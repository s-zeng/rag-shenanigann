# rag-shenanigann
Resources and documentation from my experiments in automated music composition.

You can listen to some of the results in the [samples](https://github.com/s-zeng/rag-shenanigann/tree/master/samples) folder.
Discussion about the strengths and weaknesses of this approach can be found at the end of this readme.

## Requirements
 - [midicsv](https://aur.archlinux.org/packages/midicsv/)
 - [torch-rnn](https://github.com/crisbal/docker-torch-rnn)
 - Python 3
 - (optional) [gnmidifmt](https://www.gnmidi.com/) (you'll have to use wine on linux)

The raw training data I used is included in the [rag](https://github.com/s-zeng/rag-shenanigann/tree/master/rag) folder,
and the post-processed training file can be found [here](https://github.com/s-zeng/rag-shenanigann/blob/master/samples/training_data)
in the samples folder.

## Basic steps
 1. Use [scripts/grab.py](https://github.com/s-zeng/rag-shenanigann/blob/master/scripts/grab.py) or any other method to download
 raw midi files for training data. Alternatively, use the included rag MIDIs and skip to step 3.
 2. Ensure all the MIDI files are [type 0](https://www.sweetwater.com/sweetcare/articles/what-difference-between-midi-type-0-midi-type-1/).
 Due to the nature of using a recurrent neural network for this purpose, its better to group all notes together rather then splitting
 by left/right hand. Use gnmidifmt to convert midi types, or write your own script to do it.
 3. Use [scripts/process.py](https://github.com/s-zeng/rag-shenanigann/blob/master/scripts/process.py) to turn your folder of midi
 files into a single text file. This uses midicsv to parse the midi files and extract the tempo, ticks per quarter note, and notes.
 The first two are put directly into the training file, while the notes on each tick are represented by an ascii character corresponding
 to their value. Spaces are used to separate ticks.
 4. Follow the default instructions for the torch-rnn docker file to train off the sample data created on step 3.
 5. Once trained to a satisfactory degree, use [scripts/unprocess.py](https://github.com/s-zeng/rag-shenanigann/blob/master/scripts/unprocess.py)
 to turn the output into separated csv files representing the outputted rags, then use csvmidi to convert the csv files to midi
 6. Listen and enjoy!
 
 ## Reflection
 You may have noticed a commonality in all of the sample output files - inconsistent tempo and styles.
 Perhaps inconsistent style may be unavoidable with a neural network approach, but the inconsistent tempo likely arises from not
 normalizing the tempo and ticks/beat in each midi file. Future work should focus on converting each midi file to a specific tempo
 and ticks/beat in a manner that preserves the songs actual runtime.
