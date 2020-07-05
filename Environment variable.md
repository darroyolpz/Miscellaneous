# How to permanently set an environment variable

1. Go to command line and type: nano ~/.profile
2. At the bottom of the file, add: export ENVIRONMENT_VARIABLE="VALUE_OF_ENVIRONMENT_VARIABLE"
3. Save the file and reboot the system

For using it in the code:

```python
url_wb = os.environ.get('DISCORD_WH')
```

Source: https://askubuntu.com/questions/887442/how-to-permanently-set-an-environment-variable/887479
