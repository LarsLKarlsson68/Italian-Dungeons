
trace = True

class Behavior:
    def init_memory():
        pass
    def execute():
        pass

class BehaviorMemory:
    def __init__(self,var_names,var_values):
        self.var_names = var_names
        self.var_values = var_values

class Act(Behavior):
    def __init__(self,call):
        self.call = call
    def init_memory(self,var_names,var_values):
        mem = BehaviorMemory(var_names,var_values)
        mem.call = eval('lambda '+','.join(var_names)+': '+self.call)
        return mem
    def execute(self,mem,prio,assign_s,assign_f):
        if trace:
            print prio, self.call
        mem.var_values[0].action_alternatives.append((prio, lambda : apply(mem.call, tuple(mem.var_values)),\
                                                      assign_s, assign_f))

def execute_action_alternative(alternative):
    res = alternative[1]()
    if res == True:
        do_assignments_from_behaviors(alternative[2])
    elif res == False:
        do_assignments_from_behaviors(alternative[3])
    return res
        
class Beh(Behavior):
    def __init__(self,call):
        self.call = call
        name = call.split('(')[0].split('.')
        self.arg1 = name[0]
        self.name = name[1]
        self.arguments = [self.arg1]+[ a for a in call.split('(')[1].strip(')').split(',') if a]
    def init_memory(self,var_names,var_values):
        var1_value = var_values[var_names.index(self.arg1)]
        my_var_values = [ var_values[var_names.index(p)] for p in self.arguments if p ]
        beh_def = apply(eval('lambda '+self.arg1+': '+ self.arg1+'.'+ self.name),(var1_value,))
        if len(beh_def.parameters) != len(my_var_values):
            print 'Mismatching parameters in Beh(%s).' % self.call
        mem = BehaviorMemory(beh_def.parameters+beh_def.local_vars,my_var_values+\
                                                map(lambda l: apply(l,tuple(my_var_values)), beh_def.local_var_values))
        mem.body = beh_def.body
        mem.body_mem = False
        return mem    
    def execute(self,mem,prio,assign_s,assign_f):
        if trace:
            print prio, self.call, zip(mem.var_names,mem.var_values)
        mem.body.execute(mem,prio,assign_s,assign_f)

class Task(Behavior):
    def __init__(self,prio,beh_name,*args):
        self.priority = prio
        self.beh_name = beh_name
        beh_def = apply(eval('lambda x: x.'+ beh_name),(args[0],))
        if len(beh_def.parameters) != len(args):
            print 'Mismatching parameters in Task(%d,%s,...).' % prio,beh_name
        self.mem = BehaviorMemory(beh_def.parameters+beh_def.local_vars,\
                                  list(args)+map(lambda l: apply(l,args), beh_def.local_var_values))
        self.success=[0]
        self.fail = [0]
        self.assign_t = (self.success,0,(lambda x: 1),'success=1')
        self.assign_f = (self.fail,0,(lambda x: 1),'fail=1')        
        self.mem.body = beh_def.body
        self.mem.body_mem = False    
    def execute(self):
        if trace:
            print 'Task:', self.priority, self.beh_name, zip(self.mem.var_names,self.mem.var_values)
        if not self.mem.body_mem:
            self.mem.body_mem = self.mem.body.init_memory(self.mem.var_names,self.mem.var_values)
        self.mem.body.execute(self.mem.body_mem,self.priority,[self.assign_t],[self.assign_f])
        
class BehDef:
    def __init__(self,parameters,local_vars,body):
        self.parameters = parameters.split(',')
        self.local_vars = []
        self.local_var_values = []
        for l in local_vars.split(';'):
            if l:
                try:
                    var=l[:l.index('=')].strip()
                    value=eval('lambda '+parameters+':'+l[l.index('=')+1:].strip())
                except value_error:
                    var=l
                    value==eval('lambda '+parameters+': False')
                self.local_vars.append(var)
                self.local_var_values.append(value)
        self.body = body

class When(Behavior):
    def __init__(self,*clauses):
        self.clauses = clauses
    def init_memory(self,var_names,var_values):
        mem = BehaviorMemory(self.hide_specials(var_names), var_values)
        mem.var_names.extend(['success','fail','retry'])
        mem.var_values.extend([0,0,0])
        mem.clauses = [ (eval('lambda '+','.join(var_names)+':'+c[0]), c[1], \
                         len(c) >= 3 and prepare_assignments_in_behavior(c[2],mem) or [],\
                         len(c) >= 4 and prepare_assignments_in_behavior(c[3],mem) or [],
                         len(c) >= 3 and test_if_add_previous_assignments(c[2]) or False,
                         len(c) >= 4 and test_if_add_previous_assignments(c[3]) or False                         
                         )\
                        for c in self.clauses ]
        mem.clauses_mem = [ False ]*len(mem.clauses)
        return mem
    def hide_specials(self,var_names):
        return [ v in ['success','fail','retry'] and '*' or v for v in var_names ]  
    def execute(self,mem,prio,assign_s,assign_f):
        var_tuple = tuple(mem.var_values[:-3])
        done = False
        mem.var_values[var_length-1] = False # Retry
        while not done:
            prev_action_alternatives = mem.var_values[0].action_alternatives
            done = True
            for i in range(len(mem.clauses)):
                res = apply(mem.clauses[i][0],var_tuple)
                if trace:
                    print 'when:', self.clauses[i][0], '=>', res
                if res > 0:
                    if not mem.clauses_mem[i]:
                        mem.clauses_mem[i] =mem.clauses[i][1].init_memory(mem.var_names,mem.var_values)
                    mem.clauses[i][1].execute(mem.clauses_mem[i],min(prio,res),\
                                              mem.clauses[i][2]+(mem.clauses[i][4] and assign_s or []),\
                                              mem.clauses[i][3]+(mem.clauses[i][5] and assign_f or []))
                    var_length = len(mem.var_names)
                if mem.var_values[var_length-1]: #retry - reset action alternatives
                        mem.var_values[0].action_alternatives = prev_action_alternatives
                        done = False
                        break
                    
def prepare_assignments_in_behavior(assignment_list_string,mem):
    assignment_list = assignment_list_string.split(';')
    assignments = []
    for a in assignment_list:
        var=a[:a.index('=')].strip()
        assign=a[a.index('=')+1:].strip()
        assignments.append((mem.var_values, mem.var_names.index(var),\
                            eval('lambda '+','.join(mem.var_names)+':'+assign), a))
        return assignments

def test_if_add_previous_assignments(assignment_list_string):
    return len(assignment_list_string) >= 7 and assignment_list_string[:7]=='success' or \
           len(assignment_list_string) >= 4 and assignment_list_string[:4]=='fail'

def do_assignments_from_behaviors(assignment_list):
    for a in assignment_list:
        if trace:
            print a[3]
        a[0][a[1]] = apply(a[2],tuple(a[0]))
    
class MyAgent:
    def shout(self,text):
        print text
        return True
    warn = BehDef('a,text','s=1',Act('a.shout(text)'))
    foo = BehDef('a','s=2; t=5',When(('a.happy',Act('a.shout("Yahoo")'),'success=1'),
                                     ('not a.happy',Act('a.shout("Behehe")'),'fail=1')))
                 
def test():
    ag = MyAgent()
    ag.happy = 1
    ag.action_alternatives = [] 
##    b1 = Beh('a.warn(text)')
##    m1 = b1.init_memory(['a','text'],[ag,'Hello!'])
##    print zip(m1.var_names, m1.var_values)
##    b1.execute(m1,1,[])    
##    b2 = Beh('a.foo()')
##    m2 = b2.init_memory(['a'],[ag])
##    print zip(m2.var_names, m2.var_values)
##    b2.execute(m2,0.8,[])
    t = Task(1,'foo',ag)
    t.execute()
    execute_action_alternative(ag.action_alternatives[0])
    return t
    
