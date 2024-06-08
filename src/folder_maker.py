import os,sys


"""Making the obsidian flow for new machines"""


def note_maker(box,dir,box_ip):
    # testing to make sure the box is not new 
    new_box = os.path.join(dir,box)
    try:
        os.makedirs(new_box)
    except FileExistsError:
        print(f"Box {box} already exists")
        return
    
    for val in ['enum','exploit','loot','privesc','Things Ive Learned']:
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
        scan_dir = os.path.join(box_ip_dir,'scans')
        if not os.path.exists(os.path.join(scan_dir,'active')):
            os.makedirs(os.path.join(scan_dir,'active'))
        if not os.path.exists(os.path.join(scan_dir,'passive')):
            os.makedirs(os.path.join(scan_dir,'passive'))
    else:
        print(f"Box {os.path.join(enum_dir,'results')} already exists")

if __name__ == '__main__':
    main_doc = '{your main directory here}'
    dirs=['VulnHub','HTB']
    user_box = input("Enter the box name: ")
    user_box_ip = input("Enter the box ip, if you dont know it enter 0.0.0.0: ")
    for dir in dirs:
        working_dir = os.path.join(main_doc,dir)
        note_maker(user_box,working_dir,user_box_ip)
