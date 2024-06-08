import os 


def test_file(box,dir,box_ip):
    file_dict = {
        'enum': {'results':{f'scans_{box_ip}':['active','passive']}},
        'exploit': ['Immediate_Ideas','failed_exploits','successful_exploits'],
        'loot': [],
        'privesc': [],
        'Things Ive Learned': [],
        'screenshots': []
    
    }
    new_box = os.path.join(dir,box)
    try:
        os.makedirs(new_box)
    except FileExistsError:
        print(f"Box {box} already exists")
        return
    for key,val in file_dict.items():
        if not os.path.exists(os.path.join(new_box,key)):
            os.makedirs(os.path.join(new_box,key))
            if len(val) > 0:
                if isinstance(val,dict):
                    for k,v in val.items():
                        print(k)
                        print(v)
                        if not os.path.exists(os.path.join(new_box,key,k)):
                            os.makedirs(os.path.join(new_box,key,k))
                            if isinstance(v,dict):
                                for k1,v1 in v.items():
                                    if not os.path.exists(os.path.join(new_box,key,k,k1)):
                                        os.makedirs(os.path.join(new_box,key,k,k1))
                                        if isinstance(v1,list):
                                            for item in v1:
                                                if not os.path.exists(os.path.join(new_box,key,k,k1,item)):
                                                    os.makedirs(os.path.join(new_box,key,k,k1,item))       
                            elif isinstance(v,list):
                                for item in v:
                                    if not os.path.exists(os.path.join(new_box,key,k,item)):
                                        os.makedirs(os.path.join(new_box,key,k,item))
                                    else:
                                        pass
        
                elif isinstance(val,list):
                    for item in val:
                        if not os.path.exists(os.path.join(new_box,key,item)):
                            os.makedirs(os.path.join(new_box,key,item))
                        else:
                            pass
        else:
            pass
    

if __name__ == '__main__':
    MAIN_DOC = '<path to your docs>'
    dirs=['VulnHub','HTB']
    user_box = input("Enter the box name: ")
    user_box_ip = input("Enter the box ip, if you dont know it enter 0.0.0.0: ")
    for dir in dirs:
        working_dir = os.path.join(MAIN_DOC,dir)
        test_file(user_box,working_dir,user_box_ip)
    