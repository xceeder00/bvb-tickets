# 🤖 Telegram Bot Setup Guide

Follow these steps to create a Telegram bot and get your credentials for BVB ticket notifications.

## 📱 Step 1: Create a Telegram Bot

1. **Open Telegram** and search for `@BotFather`
2. **Start a chat** with BotFather
3. **Send the command**: `/newbot`
4. **Choose a name** for your bot (e.g., "BVB Ticket Monitor")
5. **Choose a username** for your bot (must end in 'bot', e.g., "bvb_ticket_monitor_bot")
6. **Save the Bot Token** - it looks like: `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`

## 🆔 Step 2: Get Your Chat ID

### Method 1: Using @userinfobot
1. Search for `@userinfobot` in Telegram
2. Start a chat and send any message
3. The bot will reply with your user info including your **Chat ID**

### Method 2: Using your bot
1. Send a message to your newly created bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Look for `"chat":{"id":XXXXXXXXX` - that's your Chat ID

### Method 3: Using @RawDataBot
1. Search for `@RawDataBot` in Telegram
2. Start a chat and send any message
3. Look for `"id":` in the response

## ⚙️ Step 3: Configure Your Bot

Add your credentials to the configuration:

### For Local Development (config.json):
```json
{
  "telegram": {
    "enabled": true,
    "bot_token": "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ",
    "chat_id": "123456789"
  }
}
```

### For Vercel Deployment:
Set these as environment variables in your Vercel dashboard:
- `TELEGRAM_BOT_TOKEN`: Your bot token
- `TELEGRAM_CHAT_ID`: Your chat ID

## 🧪 Step 4: Test Your Setup

### Test Locally:
```bash
python test_telegram.py
```

### Test on Vercel:
After deployment, visit: `https://your-app.vercel.app/api/monitor`

## 🔐 Security Best Practices

- ✅ **Never share your bot token publicly**
- ✅ **Use environment variables for production**
- ✅ **Regenerate tokens if compromised**
- ✅ **Only share your Chat ID with trusted services**

## 🎯 Expected Bot Behavior

When tickets are available, you'll receive a message like:

```
🎫 BVB TICKETS AVAILABLE! 🟡⚫

October 4th Match - Act Fast!

🕐 Detected: 2024-10-01T14:30:00
🎯 Empty State Active: false
📍 Status: ✅ TICKETS AVAILABLE!

🔗 Buy Tickets NOW!

⚡ Don't wait - tickets sell out fast!
```

## 🛠️ Troubleshooting

### "Unauthorized" Error:
- Check your bot token is correct
- Make sure you've started a chat with your bot

### "Chat not found" Error:
- Verify your Chat ID is correct
- Ensure you've sent at least one message to your bot

### No notifications received:
- Check the Vercel function logs
- Verify environment variables are set correctly
- Test the `/api/monitor` endpoint manually

## 📞 Need Help?

1. Double-check your bot token and chat ID
2. Test with a simple message first
3. Check Vercel deployment logs
4. Ensure `.empty-state` element exists on the target page
