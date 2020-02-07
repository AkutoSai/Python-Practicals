class Intern():
    e_count = 0
    def __init__(self,name,stipend):
        self.name = name
        self.stipend = stipend
        Intern.e_count += 1

    def get_intrn_data(self):
        return 'Name: {}\nstipend: {}'.format(self.name,self.stipend)

class Qualification():
    q_count = 0
    def __init__(self,degree,experience):
        self.degree = degree
        self.exp = experience
        Qualification.q_count += 1

    def get_qualification(self):
        return 'Degree: {}\nExperience: {}'.format(self.degree,self.exp)

class Analyst(Intern,Qualification):
    s_count = 0
    def __init__(self,name,stipend,degree,experience,domain):
        Analyst.s_count += 1
        Intern.__init__(self,name,stipend)
        Qualification.__init__(self,degree,experience)
        self.domain=domain

    def get_Analyst_details(self):
        return '{}\n{}\nDomain: {}\nIntern count:{}\nQualification count:{}\nAnalyst count:{}'.format(self.get_intrn_data(),self.get_qualification(),self.domain,Intern.e_count,Qualification.q_count,self.s_count)

class Manager(Intern,Qualification):
    m_count = 0
    def __init__(self,name,stipend,degree,experience):
        Manager.m_count += 1
        Intern.__init__(self,name,stipend)
        Qualification.__init__(self,degree,experience)

    def get_Analyst_details(self):
        return '{}\n{}\nIntern count:{}\nQualification count:{}\nManager count:{}'.format(self.get_intrn_data(),self.get_qualification(),Intern.e_count,Qualification.q_count,self.m_count)


Analyst = Analyst("Prateek","30000","PhD",11,"Business Analyst")
print('\nAnalyst Details:\n')
print(Analyst.get_Analyst_details())
print('\n\nManager Details:\n')
manager = Manager("Divyansh","25000","Media Analyst",2)
print(Manager.get_Analyst_details())