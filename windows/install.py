import os,sys

appname =  sys.argv[1]

print  appname
base_dir = os.path.join(os.curdir ,appname)
app_dir =   os.path.join(base_dir,[o for o in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir,o))][0])

print base_dir,app_dir
d=app_dir
print os.listdir(app_dir)
fr=file(os.path.join( app_dir,'settings.py'))
fwrite=file('settings.py','w')
line =  fr.readline()
secret_key=""
while line:
    if 'SECRET_KEY'  in  line:
        secret_key = line

    elif 'ROOT_URLCONF' in line:
        root_urlconf = line

    elif 'WSGI_APPLICATION' in line:
        wsgi_application = line        
        #break
    line = fr.readline()

fr.close()

fr=file('setting.txt')

line = fr.readline()
while line:
    if 'SECRET_KEY' in line:
        fwrite.write(secret_key)

    elif 'ROOT_URLCONF' in line:
        fwrite.write(root_urlconf)

    elif 'WSGI_APPLICATION' in line:
         fwrite.write(wsgi_application  )    
    else:
        fwrite.write(line)
    line=fr.readline()        

fwrite.close()
fr.close()

