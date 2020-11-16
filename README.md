# login_module
Custom OAuth Module

Build instructions:
1. Build the image:
    ```
    docker image build -t open_oauth_image <location of dockerfile>
    ```
2. Build the container:
    ```
    docker container run -itd \
        --name open_oauth_image \
        -p 0.0.0.0:8000:8000
        -v <absolute_path_to_workdir>:/app/
        open_oauth_image
    ```
