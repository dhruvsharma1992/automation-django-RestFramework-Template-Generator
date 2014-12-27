(django-admin  startproject %1 ) && ( xcopy  modules\* %1\%1 /E /Y) && ( python install.py %1) &&   ( copy  settings.py  %1\%1)  && ( cd %1 ) && ( python manage.py migrate ) && ( cd .. )  
