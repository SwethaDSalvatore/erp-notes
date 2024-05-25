# Copyright (c) 2024, swetha and contributors
# For license information, please see license.txt

  #   def validate(self):
  #      frappe.msgprint("Vannako da mappule")
     
  #  def before_save(self):
  #     frappe.throw("save pannilaamaa?")
    
  #before_insert
  #after_instert  - validate befor savaing data to db
  #on_update - trigger while updating anything
  #on_submit
  #on_trash - trigger at the time of deleting
  #after_delete - trigger after deleting

 # def validate(self):
 #      full_name = self.first_name+" "+self.middle_name+" "+self.last_name
 #      self.set("full_name",full_name)

 #      array_Of_Members = self.get("family_members")
 #      total_salary = 0
 #      for member in array_Of_Members:
 #       total_salary+=member.salary
 #      self.set('total_salary', total_salary)  

# get doc ############################ 
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):

#   def validate(self):
      
#       array_Of_Members = self.get("family_members")
#       total_salary_server = 0
#       for member in array_Of_Members:
#        total_salary_server+=member.salary
#       self.set('total_salary_server', total_salary_server)  

#       self.get_document()
#       total = total_salary_server + client_side_salary_total
#       self.set("total_salary",total)
      
#   def get_document(self):
#       doc = frappe.get_doc("Client Side Scripting", self.client_side_scripting)
#       full_name = doc.full_name
#       frappe.msgprint(full_name)
#       self.set("full_name",full_name)
#       client_salary = doc.total_salary
#       # frappe.msgprint(str(client_salary))
#       self.set("client_side_salary_total",client_salary)

    # def validate(self):
    #  self.get_document()
    # def get_document(self):
    #      doc = frappe.get_doc("Client Side Scripting", self.client_side_scripting)
    #      for row in doc.get("family_members"):
    #          frappe.msgprint(row.name1)



# new doc ###########################################
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):

#     def validate(self):
#      self.new_document()  

#     def new_document(self):
#        doc = frappe.new_doc("Client Side Scripting") 
#        doc.first_name= "alice"
#        doc.last_name="arpudha"
#        doc.age=13
      
#        doc.append("family_members",{ 
#           "name1":"sivaji",
#           "relation":"summa",
#           "age":12,
#           "salary":200
#          },
#          )
#        doc.insert()

 # delete doc ########################################### 
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):

#     def validate(self):
#         frappe.delete_doc("Client Side Scripting","PR-0003")



#get_list ##################################################    
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):    
    
  
#  def validate(self):
#   self.get_list()

#  def get_list(self):
#   doc = frappe.db.get_list('Client Side Scripting',
#                            filters={
#                             'enable': 1
#                            },
#                            fields=['age','first_name']
#                            ) 
#   for d in doc:
#    age=str(d['age'])
#    first_name= d['first_name'] if d['first_name'] else 'unknown'
#    frappe.msgprint(f"Age:{age}, first Name: {first_name}")

# get value #####################################################
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         self.get_value()

#     def get_value(self):
#         doc = frappe.db.get_value('Client Side Scripting','PR-0011',['first_name','age'])

#         first_name, age = doc if doc else (None, None)
#         first_name= first_name if first_name else 'Unknown'
#         age= str(age) if age is not None else 'N/A'
#         frappe.msgprint(f"Age:{age}, first Name:{first_name}")

# set value ######################################################

# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         self.set_value()

#     def set_value(self):
#         frappe.db.set_value('Client Side Scripting','PR-0011','first_name', 'sam')
#         first_name, age = frappe.db.get_value('Client Side Scripting','PR-0011',['first_name','age'])
#         frappe.msgprint(f"first Name:{first_name}, Age:{age}")  

# get and set list of value ###########################################

# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         self.set_value()
#         self.get_value()

#     def set_value(self):
#       frappe.db.set_value('Client Side Scripting','PR-0011',{
#          "first_name":"sweamaa",
#          "age":25
#       })

#     def get_value(self):
#        doc = frappe.db.get_value('Client Side Scripting', 'PR-0011', ['first_name', 'age'])
#        first_name, age = doc if doc else (None, None) 
#        first_name = first_name if first_name else 'Unknown'
#        age = str(age) if age is not None else "N/A"
#        frappe.msgprint(f"Age:{age}, first Name:{first_name}")

# exists() ##################################################

# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         if frappe.db.exists('Client Side Scripting','PR-0011'):
#             frappe.msgprint("doc irukuu!!")
#         else :
#             frappe.msgprint("onnum illa")
        

# count() ########################################################
# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         frappe_doc= frappe.db.count('Client Side Scripting',{'enable':1})
#         frappe.msgprint(str(frappe_doc))


# sql() ###########################################################

# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
    
#     def validate(self):
#         self.sql()

#     def sql(self):

#         data= frappe.db.sql("""
#                             SELECT
#                              first_name,
#                              age
#                             FROM
#                              `tabClient Side Scripting`
#                             WHERE
#                                enable = 1
#                             """, as_dict=1)    
#         for d in data:
#             # frappe.msgprint(f"First Name:{d['first_name']} Age:{str(d['age'])}")
#             ### or ###
#             frappe.msgprint(f"First Name:{d.first_name} Age:{str(d.age)}")


# frm.call() #####################################################################

# import frappe
# from frappe.model.document import Document

# class ServerSideScripting(Document):
#   pass
    # @frappe.whitelist()
    # def frm_call(self,msg):
    #     # import time
    #     # time.sleep(5)
    #     # frappe.msgprint(msg)

    #     # self.first_name='alvin'
    #     return "hIII"