import os
import json
import datetime

class GroupMember:
    def __init__(self, id:int, username:str, messages:list) -> None:
        self.id= id
        self.username = username
        self.messages = messages
        
    def add_message(self, new_message):
        self.messages.append(new_message)

    def get_top_words(self)->list:
        topwords = dict()
        for message in self.messages:
            for word in message["text"].split():
                if topwords.get(word) == None:
                   topwords[word] = 1
                else:
                    topwords[word] += 1

        result = []
        for k, v in topwords.items():
            result.append({
                "word": k,
                "count": v
            })
        result = sorted(result, key=lambda x: x["count"], reverse=True)
        return result
    
    def get(self)->object:
        return {
            "id": self.id,
            "username": self.username,
            "messages": self.messages,
            "top_words": self.get_top_words()
        }


class Group:
    def __init__(self, id:int, name) -> None:
        self.id = id
        self.name = name
        self.members = dict()
        self.load()

    def load(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_path = f"files/{self.id}_{current_date}.json"
        if not os.path.exists(file_path):
            data = {
                "id": 0,
                "name": "",
                "members": []
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        finally: 
            for member in data['members']:
                self.members[member["id"]] = GroupMember(member["id"], member["username"], member["messages"])
        
    def get(self):
        group = {
            "id":self.id,
            "name":self.name,
            "members": []
        }
        print(self.members)
        for k, member in self.members.items():
            group['members'].append(member.get())
        return group

    def save(self):
        data = self.get()
        print(data)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_path = f"./files/{self.id}_{current_date}.json"
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def addMessage(self, newmessage: object):
        if self.members.get(newmessage['member']['id']) == None:
            self.members[newmessage['member']['id']] = GroupMember(newmessage['member']['id'], newmessage['member']["username"], [])
        self.members[newmessage['member']['id']].add_message(newmessage)
