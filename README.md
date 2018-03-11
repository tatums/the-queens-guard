# The Queens Guard ![guard](./guard.png)

This repository contains scripts and resources for a raspberry pi to record
when a door is opened.

```
Door opens
  |> raspberry pi reads this via the GPIO pins
  |> the pi records this in a DynamoDB
```

ENV variables
```
export STACK_NAME="the-queens-guard"
```

```
aws cloudformation create-stack \
    --stack-name $STACK_NAME
    --template-body file://./cloudformation.yml && \

    aws cloudformation wait stack-create-complete \
        --stack-name $STACK_NAME
```


## startup on boot

The raspberri pi starts python script using `/etc/rc.local`
```
# /etc/rc.local
sudo /usr/bin/python /home/pi/the-queens-guard/gate-guard/monitor.py &
```
