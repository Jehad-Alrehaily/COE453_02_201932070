const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World, from gcloud GCP Cloud Run');
    });


    app.post('/', (req, res) => {
        if (req.body) {
            // Parse the JSON from the request body
            const requestBody = req.body;
            const x = req.body.x;
            const y = req.body.y
            const result = x - y;
            // Create a JSON response object
            const responseObject = {
              // message: `Hello to COE 453 from GCP Cloud functions, you sent: ${JSON.stringify(requestBody)}`
            "x": x,
            "y":y,
            "result":result
        
            };
        
            // Send the JSON response
            res.json(responseObject);
          } else {
            // If no body is found in the request
            res.status(400).send('No JSON body found in the request.');
          }
                });



app.listen(8080, () => {
    console.log('Server is up on 8080');
    }
);