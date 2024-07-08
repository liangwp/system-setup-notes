# FROM nvidia/cuda:11.2.2-base-ubuntu20.04
# FROM python:3.10-bullseye
# FROM python:3.11-slim-bullseye
FROM python:3.11-slim-bookworm

# RUN pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
# RUN pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
# RUN pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
# RUN pip3 install torch==2.0.0+cu118 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


WORKDIR /workspace
COPY ./main.py /workspace/

# CMD [ "nvidia-smi" ]
CMD [ "python", "main.py" ]
