import os,sys


"""Making the sublime flow for new  boxes and the obsidian flow"""
def note_maker(box,dir,box_ip):
    # testing to make sure the box is not new 
    new_box = os.path.join(dir,box)
    try:
        os.makedirs(new_box)
    except FileExistsError:
        print(f"Box {box} already exists")
        return  
    # making the box in the subl vault
    if 'sublime' in new_box:
        for val in ['enum','exploit','loot','privesc']:
            if not os.path.exists(os.path.join(new_box,val)):
                os.makedirs(os.path.join(new_box,val))
            else:
                print(f"Box {box} already exists")
        enum_dir = os.path.join(new_box,'enum')
        if not os.path.exists(os.path.join(enum_dir,'results')):
            results = os.path.join(enum_dir,'results')
            os.makedirs(os.path.join(results,box_ip))
            box_ip_dir = os.path.join(results,box_ip)
            for val in ['exploits','loot','scans']:
                if not os.path.exists(os.path.join(box_ip_dir,val)):
                    os.makedirs(os.path.join(box_ip_dir,val))
    elif 'obsidian' in new_box:
        for vals in ['enum','exploit','loot','privesc','Things Ive Learned']:
            if not os.path.exists(os.path.join(new_box,vals)):
                os.makedirs(os.path.join(new_box,vals))
            else:
                print(f"Box {box} already exists")
        enum_dir = os.path.join(new_box,'enum')
        if not os.path.exists(os.path.join(enum_dir,'results')):
            results = os.path.join(enum_dir,'results')
            os.makedirs(os.path.join(results,box_ip))
            box_ip_dir = os.path.join(results,box_ip)
            for val in ['exploits','loot','scans']:
                if not os.path.exists(os.path.join(box_ip_dir,val)):
                    os.makedirs(os.path.join(box_ip_dir,val))
    else:
        print("Please specify the box type")
    

if __name__ == '__main__':
    print(__name__)
    dirs=['/Users/deangelofloyd/Documents/sublime_data','/Users/deangelofloyd/Documents/obsidian_files/HTB_Machines']
    user_box = input("Enter the box name: ")
    user_box_ip = input("Enter the box ip, if you dont know it enter 0.0.0.0: ")
    for dir in dirs:
        note_maker(user_box,dir,user_box_ip)
