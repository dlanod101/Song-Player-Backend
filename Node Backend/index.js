import express from 'express';
import bodyParser from 'body-parser';
import multer from 'multer';
import fs from 'fs';
import path from 'path';

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());

// Ensure 'uploads/' and 'uploads/images/' exist
const uploadDirs = ['uploads/songs', 'uploads/images'];
uploadDirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
});

// Configure Multer Storage for Songs & Images
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        if (file.mimetype.startsWith('audio/')) {
            cb(null, 'uploads/songs/');
        } else if (file.mimetype.startsWith('image/')) {
            cb(null, 'uploads/images/');
        } else {
            cb(new Error('Invalid file type'), null);
        }
    },
    filename: (req, file, cb) => {
        cb(null, `${Date.now()}-${file.originalname}`);
    }
});

const upload = multer({ storage });

let songs = [];

// GET ALL SONGS
app.get('/songs', (req, res) => {
    res.json(songs);
});

// GET RANDOM SONG
app.get("/random", (req, res) => {
    const randomIndex = Math.floor(Math.random() * songs.length);
    res.json(songs[randomIndex]);
});

// GET SPECIFIC SONG
app.get("/songs/:id", (req, res) => {
    const songId = parseInt(req.params.id);
    const foundSong = songs.find(song => song.id === songId);
    res.json(foundSong);
});

// GET SONGS BY GENRE
app.get("/filter", (req, res) => {
    const genre = req.query.genre;
    const filteredSongs = songs.filter(song => song.songGenre === genre);
    res.json(filteredSongs);
});

// ADD A SONG WITH AUDIO & IMAGE UPLOAD
app.post("/create", upload.fields([{ name: 'songFile', maxCount: 1 }, { name: 'coverImage', maxCount: 1 }]), (req, res) => {
    if (!req.files['songFile'] || !req.files['coverImage']) {
        return res.status(400).json({ message: "Both song file and cover image are required." });
    }

    const newSong = {
        id: songs.length + 1,
        songName: req.body.songName,
        artist: req.body.artist,
        songGenre: req.body.songGenre,
        songLength: req.body.songLength,
        songFile: req.files['songFile'][0].path,  // Save song file path
        coverImage: req.files['coverImage'][0].path // Save cover image path
    };

    songs.push(newSong);
    res.status(201).json(newSong);
});

// EDIT A SONG (Metadata, Audio, and Image Upload)
app.patch("/update/:id", upload.fields([{ name: 'songFile', maxCount: 1 }, { name: 'coverImage', maxCount: 1 }]), (req, res) => {
    const songId = parseInt(req.params.id);
    const existingSong = songs.find(song => song.id === songId);

    if (!existingSong) {
        return res.status(404).json({ message: "Song not found" });
    }

    existingSong.songName = req.body.songName || existingSong.songName;
    existingSong.artist = req.body.artist || existingSong.artist;
    existingSong.songGenre = req.body.songGenre || existingSong.songGenre;
    existingSong.songLength = req.body.songLength || existingSong.songLength;

    if (req.files['songFile']) {
        existingSong.songFile = req.files['songFile'][0].path;
    }
    
    if (req.files['coverImage']) {
        existingSong.coverImage = req.files['coverImage'][0].path;
    }

    res.status(200).json(existingSong);
});

// DELETE A SONG
app.delete("/delete/:id", (req, res) => {
    const songId = parseInt(req.params.id);
    const index = songs.findIndex(song => song.id === songId);

    if (index > -1) {
        songs.splice(index, 1);
        res.status(200).json({ message: `Song with id ${songId} deleted.` });
    } else {
        res.status(404).json({ message: "Song not found. No song deleted." });
    }
});

// DELETE A LIST OF SONGS
app.delete("/delete/list", (req, res) => {
    const { songIds } = req.body;

    if (!Array.isArray(songIds) || songIds.length === 0) {
        return res.status(400).json({ message: "Invalid request. Provide an array of song IDs." });
    }

    let deletedSongs = [];
    let notFoundSongs = [];

    songIds.forEach(id => {
        const index = songs.findIndex(song => song.id === id);
        if (index > -1) {
            deletedSongs.push(songs[index]);
            songs.splice(index, 1);
        } else {
            notFoundSongs.push(id);
        }
    });

    let responseMessage = {
        deleted: deletedSongs.map(song => song.id),
        message: `Deleted ${deletedSongs.length} song(s).`
    };

    if (notFoundSongs.length > 0) {
        responseMessage.notFound = notFoundSongs;
        responseMessage.message += ` ${notFoundSongs.length} song(s) not found.`;
    }

    res.status(200).json(responseMessage);
});

// DELETE ALL SONGS
app.delete("/delete/all_songs", (req, res) => {
    songs = [];
    res.status(200).json({ message: "All songs deleted successfully." });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
