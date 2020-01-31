FROM python:buster

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_12.x
# Ref: https://yarnpkg.com/en/docs/install
RUN \
  echo "deb https://deb.nodesource.com/node_12.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs yarn && \
  pip install -U pip && pip install pipenv && \
  npm i -g npm@^6 && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update -qq; \
    apt-get -qq remove postgis; \
    apt-get install -y --fix-missing --no-install-recommends \
        software-properties-common \
        apt-transport-https ca-certificates gnupg software-properties-common wget

RUN apt-get install binutils libproj-dev gdal-bin -y

# install node packages
WORKDIR /usr/src/app/dashboard
COPY dashboard/package.json .
RUN npm install

# build react project
COPY dashboard/ ./
RUN yarn build

# install python packages
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt

# setup python project
COPY . .

EXPOSE 8000

#RUN python manage.py collectstatic --no-input
#RUN python manage.py makemigrations
#RUN python manage.py migrate

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
