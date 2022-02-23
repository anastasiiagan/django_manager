**Final Manager** (FM) odpowiada za usuwanie kontenerów o określonej nazwie.
Przyjęlam, że nasze aplikacje będą mieć strukturę nazwy **'f_app_' + {app_id}**

W folderze *dj_dock_train* jest prosta aplikacja w django.
Aby przetestować FM, należy utworzyć kilka aplikacji w Dockerzy. Najpierw trzeba zbuildować image z tego folderu za pomocą komendy
> docker build --tag i_f_app_0 .

Następnie należy postawić kilka kontenerów na podstawie tego imege-a 
> docker run -d --publish 8000:8000 --name f_app_0 i_f_app_0
> docker run -d --publish 8000:8000 --name f_app_1 i_f_app_0
> docker run -d --publish 8000:8000 --name f_app_2 i_f_app_0

Teraz mamy dzialające kontenery {f_app_0, f_app_1, f_app_2}

W folderze *final_manager* trzeba uruchomić aplikację przy pomocy komendy
> docker-compose up

w osobnym terminalu możemy przetestować dostępne metody **list** oraz **delete** przy pomocy
>curl -X GET http://0.0.0.0:5005/f-manager/list
>curl -X DELETE http://0.0.0.0:5005/f-manager/delete/0

*W docker-compose.yml trzeba zmienić odpowiednio DOCKER_API_PORT oraz DOCKER_API_URL - są różne dla każdego urządzenia*