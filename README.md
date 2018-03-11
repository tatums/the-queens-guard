# The Queens Guard ![](./guard.png)

This repository contains scripts and resources for an arduino to record when a door is opened.

```
Door opens
  |> raspberry pi reads this via the GPIO pins
  |> the pi, in python, executes an AWS lambda
  |> Lambda records this in a data-store
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
