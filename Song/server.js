const express = require('express');
const multer = require('multer');
const xlsx = require('xlsx');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

let songData = [];

app.use(express.static('public'));

// Endpoint to upload and process the Excel file
app.post('/upload', upload.single('file'), (req, res) => {
    const filePath = path.join(__dirname, req.file.path);
    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    songData = xlsx.utils.sheet_to_json(sheet);
    fs.unlinkSync(filePath); // Delete the file after processing
    res.send('File uploaded and data processed.');
});

// Endpoint to get the song data
app.get('/songs', (req, res) => {
    res.json(songData);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
