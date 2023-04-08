# openai-telegram-bot

Soviet Code game Telegram Bot

## Configuration

### Zappa configuration

Rename `zappa_settings.template.json` to `zappa_settings.json` and update the parameters like
`arn`, `s3_bucket`, `aws_region`.

### Bot configuration

1. Create a new bot, get its API key and put to
   TELEGRAM_API_KEY environment variable

## Running locally

1. Setup ngrok: `ngrok http 5001`

2. Update .env file with:
   ```
   TELEGRAM_API_KEY=<your bot API key>
   WEBHOOK_HOST=<ngrok url>
   ```

3. Run the app:

```
flask --debug run --host=0.0.0.0 --port 5001
```

