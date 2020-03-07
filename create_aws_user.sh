# Simple shell script to create a user on AWS with an initial password (required to be changed) and add user to the required group


#!/bin/bash
set -e

username=<your_username>
password=<your_password>

create_user() {

  user=${1}
  password=${2}
  group=${3}

  aws iam create-user --user-name ${user}
  aws iam create-login-profile --user-name ${user} --password ${password} --password-reset-required
  aws iam add-user-to-group --user-name ${user} --group-name ${group}
}

AWS_PROFILE=<your_profile> create_user ${username} ${password} <your_group>
