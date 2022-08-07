Cloudformation Batch Jobs & Slack Alert for Failed Job Events
===
<div align="center">
<p>
   <img width="850" src="https://github.com/rayjan0114/infra/tree/main/aws_batch_event_sns_lambda/res/template-designer.png"></a>
</p>
</div>


### Setup
```
brew tap aws/tap
brew install aws-sam-cli

poetry install
```


### Deploy
```
# first time
python3 cron.py > template.yaml; sam build; sam deploy --profile yourprofile --guided;
# or
python3 cron.py > template.yaml; sam build; sam deploy --profile yourprofile;
```

