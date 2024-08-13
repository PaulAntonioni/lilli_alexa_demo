const express = require('express');
const app = express();
app.use(express.json());

app.post('/alexa-skill', (req, res) => {
    const userId = req.body.user_id;
    // Simulate Alexa asking the user if they're okay
    console.log(`Alexa is asking user ${userId} if they are okay.`);
    res.json({ status: "Alexa prompted the user" });
});

app.listen(3000, () => {
    console.log('Alexa Skill Server is running on port 3000');
});
