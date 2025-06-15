# sample entry: /home/alireza/SG/mars/general-market
# read path
path='/home/asa/mars/general-market'
cd $path
pwd
sudo systemctl stop postgresql

title1="treasury-ui"
title2="treasury-service"
title3="treasury-gateway"
title4="main-service"
title5="main-gateway"

cmd1="cd $path && cd treasury/webapp/ui/main && yarn start"
cmd2="cd $path && cd treasury/service && go run cmd/service/main.go"
cmd3="cd $path && cd treasury/webapp && go run cmd/gateway/main.go"
cmd4="cd $path && cd main/service && go run cmd/service/main.go"
cmd5="cd $path && cd main/webapp && go run cmd/gateway/main.go"

# echo
# echo -e "\e[1;37;41m        We are all Zavareh's Soldiers        \e[0m"
# echo

pwd

gnome-terminal --tab --title="$title1" --command="bash -c '$cmd1; $SHELL'" \
               --tab --title="$title2" --command="bash -c '$cmd2; $SHELL'" \
               --tab --title="$title3" --command="bash -c '$cmd3; $SHELL'" \
               --tab --title="$title4" --command="bash -c '$cmd4; $SHELL'" \
               --tab --title="$title5" --command="bash -c '$cmd5; $SHELL'" 
