import json
import re

class IPException(Exception):
    def __init__(self, message="Invalid IP Address format"):
        self.message = message
        super().__init__(self.message)

class Application:
    
    def user_credentials(self):
        credentials=['','','']
        credentialslist=[]
        try:
            user_name = input("Please enter your username: ")
            user_password = input("Please enter your password: ")
            user_IP_address = input("Please enter your IP address: ")
            credentials[0]=user_name
            credentials[1]=user_password
            credentials[2]=user_IP_address
            # format logic for IPAddress from https://www.csestack.org/validate-ip-address-regex-python/
            pattern = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)|.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)|.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)|.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'

            if(re.search(pattern, user_IP_address)): 
                # Adding Credentials to the file - SessionLogger.txt
                with open('SessionLogger.txt','a') as credentialsfile:
                    credentialsfile.writelines(user_name+"\t"+user_password+"\t"+user_IP_address+"\n")


            else: 
                raise IPException;
            credentialslist.append(credentials)


        except IPException as e:
            print(f"Error: {e}")


    def run(self):
        self.user_credentials()

if __name__ == "__main__":
    app = Application()
    app.run()


