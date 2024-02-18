from utils import *
import xml.etree.ElementTree as ET
from ipywidgets import FloatProgress

#----------------------------------------------------------------------------------
def replaceTheseChords(mySequence, verbose = False):
    #natures {'maj', 'm', 'm6', 'm7', 'dom_7', 'maj7', 'maj6', 'o7', 'o', 'sus', 'sus2', 'sus7', 'ø7', 'power', 'm_maj7'}

    correct_this = {'minor-11th': 'm add 11',
                    'dominant-ninth': 'dom7 add 9',
                    'dominant-13th': 'dom7 add 13',
                    'dominant-11th': 'dom7 add 11',
                    'diminished': 'o',
                    'minor-ninth': 'm7 add 9',
                    'none': 'N.C.',
                    #'power': 'power',
                    'major-sixth': 'maj6',
                    'diminished-seventh': 'o7',
                    'major-ninth': 'maj7 add 9',
                    'minor-sixth': 'm6',
                    'alter b9': 'dom7 add b9',
                    'minor': 'm',
                    'major-seventh': 'maj7',
                    'dominant': 'dom7',
                    'minor-seventh': 'm7',
                    'major': 'maj',
                    'augmented': 'aug',
                    'diminished-maj-seventh': 'o_maj7',
                    'suspended-fourth': 'sus4',
                    'minor-add-ninth': 'm add 9',
                    'add 4 subtract 3 add b9 add 4 subtract 3 add b9 alter #5': 'sus7 add #5 add b9',
                    'add b9 add 4 subtract 3 add b9 add 4 subtract 3': 'sus7 add b9',
                    'add 4 subtract 3 add b9 add 4 subtract 3': 'sus7 add b9',
                    'add b9 add 4 subtract 3 add #9 alter #5': 'sus7 add b9',
                    'add b9 add 4 subtract 3 add b9 alter #5': 'sus7 add b9',
                    'add 4 subtract 3 add 4 subtract 3': '',
                    'add 4 subtract 3 add b9 alter #5': 'sus7 add b9',
                    'alter #5 add b9 add 4 subtract 3': 'sus7 add b9',
                    'add 4 subtract 3 add #9 alter #5': 'sus7 add b9',
                    'add #9 alter b5 add #9 alter b5': 'alter b5 add #9',
                    'add b9 alter b5 add b9 alter b5': 'alter b5 add b9',
                    'add #11 add #11 add #11 add #11': 'add #11',
                    'add #9 alter #5 add b9 alter #5': 'add b9 alter #5',
                    'add b9 add 4 subtract 3 add b9': 'sus7 add b9',
                    'add #11 add #9 add #11 add #9': 'add #11 add #9',
                    'add 7 add b9 add 4 subtract 3': 'sus7 add b9',
                    'add 4 subtract 3 alter #11': 'sus7 add #11',
                    'alter b5 alter b5 alter b5': 'alter b5',
                    'add 4 subtract 3 alter #5': 'sus7 add #5 add b9',
                    'alter b5 add 4 subtract 3': 'sus4 add b9',
                    'alter #5 add 4 subtract 3': 'sus4',
                    'add 4 subtract 3 alter b5': 'sus4 add b9',
                    'add 4 subtract 3 alter b9': 'sus4 add b9',
                    'add 4 subtract 3 add #11': 'sus4 add #11',
                    'add #11 add b9 alter #11': 'sus7 add b9',
                    'add 4 subtract 3 add b13': 'sus4 add b9',
                    'alter #5 add #9 alter #5': 'alter #5 add #9',
                    'alter b5 add b9 alter b5': 'alter b5 add b9',
                    'add b13 add 4 subtract 3': 'sus7 add b9',
                    'add #11 add 4 subtract 3': 'sus7',
                    'add 4 subtract 3 add #9': 'sus7 add b9',
                    'add 4 subtract 3 add b9': 'sus7 add b9',
                    'add b9 add 4 subtract 3': 'sus7 add b9',
                    'add #11 add #11 add #11': 'add #11',
                    'add #11 add b9 add #11': 'add b9 add #11',
                    'add b9 add b9 alter #5': 'alter #5 add b9',
                    'add 4 subtract 3 add 9': '',
                    'add 4 subtract 3 add 7': 'sus7',
                    'add #9 alter #5 add #9': 'alter #5 add #9',
                    'add b9 alter #5 add b9': 'alter #5 add b9',
                    'add b9 alter #5 add #9': 'alter #5 add #9',
                    'add b13 add b9 add b9': 'add b9 add b13',
                    'add 9 add #11 add b9': 'add 9 add #11',
                    'add b9 add b9 add b9': 'add b9',
                    'alter #11 alter #11': 'alter #11',
                    'add b9 add b9 add 9': 'add b9',
                    'add 9 add b9 add b9': 'add b9',
                    'add 9 add #7 add 9': 'add #7 add 9',
                    'add 9 add 9 add 9': 'add 9',
                    'alter b5 alter b5': 'alter b5',
                    'alter #5 alter #5': 'alter #5',
                    'alter b5 alter #5': 'alter b5',
                    'alter #5 alter b5': 'alter #5',
                    'alter b9 alter b9': 'alter b9',
                    'add 7 add 7 add 7': 'add 7',
                    'add 4 subtract 3': '',
                    'add b13 add b13': 'add b13',
                    'add #11 add #11': 'add #11',
                    'add b9 add b9': 'add b9',
                    'add b9 add #9': 'add b9',
                    'add #7 add #7': 'add #7',
                    'add #9 add #9': 'add #9',
                    'add b6 add b6': 'add b6',
                    'add #9 add b9': 'add b9',
                    'add 9 add #9': 'add #9',
                    '*..........*': '',
                    'add b9 add 9': 'add b9',
                    'add 9 add b9': 'add b9',
                    'add 9 add 9': 'add 9',
                    'add 2 add 2': 'add 9',
                    'add 7 add 2': 'add 7 add 9',
                    'add 7 add 7': 'add 7',
                    'dim(maj7)': 'o_maj7',
                    '7susadd3': 'sus7',
                    'm(add9)': 'm7 add 9',
                    '*-add9*': 'm7 add9',
                    '7b5#5*': 'dom7 add #5',
                    '13sus4': 'sus7 add 13',
                    '*sus4*': 'sus4',
                    '7sus4': 'sus7',
                    '*mb9*': 'm7 add b9',
                    '9sus4': 'sus7 add 9',
                    '*dim*': 'o',
                    'maj13': 'maj7 add 13',
                    '*mM7*': 'm_maj7',
                    '*ø11*': 'ø7 add 11',
                    '*7+*': 'aug7', #7+
                    '*m7*': 'm7',
                    '*-3*': 'm7',
                    '6b5*': 'G dom7',
                    '7alt': '7 add b9',
                    'maj9': 'maj7 add 9',
                    '-b5*': 'm add b5',
                    '6#9*': 'maj add 6 add 9',
                    '#5#9': 'add #5 add b9',
                    '*m*': 'm7',
                    'm69': 'm add 6 add 9',
                    'm11': 'm add 11',
                    '*O*': 'o',
                    '-7s': 'm_maj7',
                    '**': 'maj', #be careful to fix maj and also include itself in the list
                    'G7': 'G dom7', #think how to fix this one
                    '69': 'maj add 6 add 9',
                    'E*': 'E',
                    'm9': 'm7 add 9',
                    '11': 'dom7 add 77',
                    'A*': 'A',
                    'G*': 'G',
                    '13': 'dom7 add 13',
                    '+7': 'dom7',
                    'C*': 'C',
                    '6': 'maj add 6',
                    '9': 'dom7 add 9',
                    '7': 'dom7',
                    '+': 'aug',
                    '5': 'power'
                    }
    sequence = []
    durations = []
    
    for song in tqdm(mySequence):
        tmp = []
        tmp_d = []  
        for item in song:
            element = item[0]  
            e_duration = item[1]          
            for key, value in correct_this.items():
                if key == element:
                    if (verbose):
                        print(element, '-->', value)
                    element = element.replace(key, value)
                    break
            tmp.append(element)
            tmp_d.append(e_duration)
        
        #check the case of 'G dom7' and split it into two
        if 'G dom7' in tmp:
            for i, n in enumerate(tmp):
                if n == 'G dom7':
                    tmp[i] = 'G'
                    tmp.insert(i+1, 'dom7')
                    tmp_d.insert(i+1, tmp_d[i])
         
        sequence.append(tmp)
        durations.append(tmp_d)
        
    #Unify the dataset again
    result = []
    for chords_values, durations_values in zip(sequence, durations):
        coupled = list(zip(chords_values, durations_values))
        result.append(coupled)
    
    #clean repeated ones
    for x, song in enumerate(result):
        for y, item in enumerate(song):
            chord = item[0]
            s = chord.split(' ')
            if len(s) >= 5:
                #print(s)
                if s[1]+s[2] == s[3]+s[4]:
                    #print(x, y, chord)
                    result[x][y]=s[0]+' '+s[1]+' '+s[2]
                    #print(sequence[x][y])
                    
    return result

#------------------------------------------------------------------
def parse_info_from_XML(path, verbose = False):
    '''
    Populate a chord sequence and an durations sequence from a XML file
    '''
    chord_sequence_list = []
    duration_sequence_list = []
    meta_info_list = []
    track = 0
    for file in tqdm(os.listdir(path)):
        if(verbose): print(file)
        if (file == '.DS_Store'):
            continue
            
        song_path = path+'/'+file
        meta_info = get_metadata(song_path)
        
        tree = ET.parse(song_path)
        root = tree.getroot()

        #possible_types = ['segno', 'rehearsal', 'coda', 'words']

        bar = '|'
        song_form = ''
        tone = ''
        coda = ''
        chord = ''
        nature = ''
        extension = ''
        slash = ''
        duration = 0
        the_chord_sequence = []
        the_duration_sequence = []

        #Division is the number of ticks per quarter note
        division = int(root.find('part').find('measure').find('attributes').find('divisions').text)

        #define the Style
        style_token = '<style>'
        the_chord_sequence.append(style_token)
        the_duration_sequence.append(duration)
        the_chord_sequence.append(meta_info['style'])
        the_duration_sequence.append(duration)

        # Find all measure elements in the root
        measures = root.findall('.//measure')
        
        for measure in measures:
            #get the duration reference
            measure_number = int(measure.attrib.get('number'))
        
            #get the bars
            bar = '|'
            barline = measure.find('barline')
            if barline != None:
                repeat = barline.find('repeat')
                if repeat != None:
                    direction = repeat.attrib.get('direction')
                    if direction == 'forward':
                        bar = '|:'
                    
            #print(bar)
            measure_children = list(measure)
            for idx, child in enumerate(measure_children):
                direction = child.find('direction-type')
                if direction is not None:
                    coda = direction.find('coda')
                    if coda is not None:
                        if idx < len(measure_children) - 2:
                            if verbose: print("In track:", track, "measure:", measure_number, "coda element is at the beginning.")
                            bar = 'b||'
                        elif idx == len(measure_children) - 1:
                            if verbose: print("In track:", track, "measure:", measure_number, "coda element is at the end.")
                            bar = 'e||'
            
            #get the Form
            direction = measure.find('direction')
            if direction != None:
                direction_type = direction.find('direction-type')
               
                # # Find the <coda> element
                # coda_element = direction_type.find('.//coda')
                # if coda_element != None:
                #     print("double bar at:", track, measure_number)
                #     bar = '||'
                    
                segno = direction_type.find('segno')
                if segno != None:
                    song_form = 'Form_Segno'
                    the_chord_sequence.append(song_form)
                    the_duration_sequence.append(duration)
                
                coda = direction_type.find('coda')
                if coda != None:
                    song_form = 'Form_Coda'
                    the_chord_sequence.append(song_form)
                    the_duration_sequence.append(duration)
                    
                form = direction_type.find('rehearsal')
                if form != None:
                    song_form = 'Form_'+form.text
                    the_chord_sequence.append(song_form)
                    the_duration_sequence.append(duration)
            
            #Append bar and duration is here
            the_chord_sequence.append(bar)
            the_duration_sequence.append(duration)
            
            #get the repetition info
            barline = measure.find('barline')
            if barline != None:
                ending = barline.find('ending')
                if ending != None:
                    number = ending.attrib.get('number')
                    if number != None:
                        rep = 'Repeat_'+ str(number) #this section defines the bar to be repeated
                        the_chord_sequence.append(rep)
                        the_duration_sequence.append(duration)
                            
            #get the chords
            for harmony in measure.iter('harmony'):
                root = harmony.find('root')
                note = root.find('root-step')
                sharp = root.find('root-alter')
                kind = harmony.find('kind')
                bass = harmony.find('bass')
                
                if sharp != None:
                    sharp = sharp.text
                    if sharp == '-1': #Remember to check double sharp and double flat
                        tone = 'b'
                    elif sharp == '1':
                        tone = '#'
                    elif sharp == '0':
                        tone = ''
                
                note = note.text+tone
                #nature = kind.attrib.get('text')
                #get the nature from kind
                nature = kind.text
                #print('bar:', measure_number, 'r:', note, 'n:', nature)
                
                #get nature of the chord
                if nature == None:
                    nature = ''
                
                #get the extension
                degree = harmony.find('degree')
                extension = ''
                if degree != None:
                    for degree in measure.iter('degree'):
                        
                        degree_type = degree.find('degree-type').text
                        relatedNote = degree.find('degree-value').text
                        degree_sharp = degree.find('degree-alter').text
                        if degree_sharp == '-1':
                            relatedNote = 'b'+relatedNote
                        elif degree_sharp == '-2':
                            relatedNote = 'bb'+relatedNote
                        elif degree_sharp == '1':
                            relatedNote = '#'+relatedNote
                        elif degree_sharp == '2':
                            relatedNote = '##'+relatedNote
                            
                        extension += ' ' + degree_type + ' ' +relatedNote
                else:
                    extension = ''
                
                #----------------------------------------------------------
                #get slash chord and its alterations
                if bass != None:
                    bass_step = bass.find('bass-step').text
                    #print(bass_step)
                    bass_alter = bass.find('bass-alter')
                    if bass_alter != None:
                        bass_alter = int(bass_alter.text)
                        #print(bass_alter)
                        if bass_alter == 1:
                            bass_note = bass_step + '#'
                        elif bass_alter == -1:
                            bass_note = bass_step + 'b'
                        elif bass_alter == 2:
                            bass_note = bass_step + '##'
                        elif bass_alter == -2:
                            bass_note = bass_step + 'bb'
                        slash = '/'+bass_note
                    else:
                        slash = '/'+bass_step
                else:
                    slash = ''
                    
                chord = note + str(nature) + extension + str(slash)
                #print(chord)
                the_chord_sequence.append(chord)
                 
            #----------------------------------------------------------
            #get durations duration
            for note_element in measure.iter('note'):
                duration = int(note_element.find('duration').text) / division
                #print(duration)
                the_duration_sequence.append(duration)
                
            #this second bar is relevant to close the section
            #Find all barline elements within the measure
            barlines = measure.findall('barline')

            # Iterate through barlines and extract information
            for barline in barlines:
                repeat = barline.find('repeat')
                if repeat != None:
                    direction = repeat.attrib.get('direction')
                    if direction == 'backward':
                        bar = ':|'
                        #print(bar)
                        the_chord_sequence.append(bar)
                        the_duration_sequence.append(duration)

        track += 1
        the_chord_sequence = np.array(the_chord_sequence, dtype=object)
        the_duration_sequence = np.array(the_duration_sequence, dtype=float)

        #print(the_chord_sequence.shape, the_duration_sequence.shape)

        #divide the chords into sections base, nature, extension, slash
        #the first two elements are the style 
        the_sequence = the_chord_sequence[2:]
        the_duration = the_duration_sequence[2:]

        format = the_chord_sequence[0:2].tolist()

        duration_format = the_duration_sequence[0:2].tolist()

        the_sequence, the_duration = fmt.getArrayOfElementsInChord(the_sequence, the_duration)
        the_duration = duration_format + the_duration
        the_sequence = format + the_sequence

        #adjust the duration sequence
        the_sequence = np.array(the_sequence, dtype=object)
        the_duration = np.array(the_duration, dtype=float)
        
        chord_sequence_list.append(the_sequence)
        duration_sequence_list.append(the_duration)
        meta_info_list.append(meta_info)
    
    chord_sequence_list = np.array(chord_sequence_list, dtype=object)
    duration_sequence_list = np.array(duration_sequence_list, dtype=object)
    meta_info_list = np.array(meta_info_list, dtype=object)
    
    print(chord_sequence_list.shape, duration_sequence_list.shape, meta_info_list.shape)
    return chord_sequence_list, duration_sequence_list, meta_info_list


#----------------------------------------------------------------------------------
#This class fix all extensions to avoid redundancy and extra tokens
def fix_extensions(sequence):
    for song in tqdm(sequence):
        for i, item in enumerate(song):
            element = item[0] #extract the chord information
            c_duration = item[1] #extract the duration information
            if 'add' in element or 'alter' in element:
                #print(element)
                split = element.split(' ')
                size = len(split)
                if size > 2:
                    if size%2 == 1:
                        #print('odd', split)
                        nature = split[0]
                        #couple the nature with duration
                        coupled = (nature, c_duration)
                        song[i] = coupled
                        counter = 1 
                        for n in range(1, size-1, 2):
                            ext = split[n] + ' ' + split[n+1]
                            coupled = (ext, c_duration)
                            song.insert(i+counter, coupled)
                            counter += 1
        #need to do it separately to avoid the index out of range           
        for i, item in enumerate(song):
            element = item[0] #extract the chord information
            c_duration = item[1] #extract the duration information
            
            if 'add' in element or 'alter' in element:
                #print(element)
                split = element.split(' ')
                size = len(split)
                if size > 2:   
                    if size%2 == 0:
                        #delete the element
                        song.pop(i)
                        counter = 0
                        for n in range(0, size-1, 2):
                            ext = split[n] + ' ' + split[n+1]
                            coupled = (ext, c_duration)
                            song.insert(i+counter, coupled)
                            counter += 1
#----------------------------------------------------------------------------------
#expand the song form
def expand_song_structure(song_structure, duration_structure, id = 0, verbose = False):
    status = True
    
    if '|:' not in song_structure:
        if verbose: 
            print('No repetition data found')
            print("-----------------------------\n")    
        return song_structure, duration_structure, status
    
    #convert numpy into array
    song_structure = song_structure.tolist()
    
    if verbose: print('Length of sequence:', len(song_structure))
    #identify the location of the repetition symbols
    
    form_zone = {'start': 0, 'end': 0, id: 0}
    inner_zone = {'start': 0, 'end': 0, id: 0}
    #rest_zone = {'start': 0, 'end': 0, id: 0}
    
    #jump to the third element and save the prior information
    intro_data = song_structure[0:2]
    sequence = song_structure[2:]
    #do the same with durations
    intro_duration = duration_structure[0:2]
    duration_sequence = duration_structure[2:]
    
    #get the location of the repetition symbols
    #find :| and Repeat_
    close = []
    repeat = []
    c_id = 0
    r_id = 0
    for i, e in enumerate(sequence):
        close_repetition = {'loc': 0, 'done': False, 'id': 0}
        repeat_section = {'loc': 0, 'done': False, 'id': 0}
        if e == ':|':
            close_repetition['loc'] = i
            close_repetition['id'] = c_id
            #print(close_repetition)
            close.append(close_repetition)
            c_id += 1
        if e.startswith('Repeat'):
            repeat_section['loc'] = i
            repeat_section['id'] = r_id
            #print(repeat_section)
            repeat.append(repeat_section)
            r_id += 1
    
    if len(repeat) == 1:
        # Substring to search for
        substring = 'Repeat_'

        # Find the index of the first element containing the substring
        index = next((i for i, element in enumerate(sequence) if substring in element), None)
        #erase the location element
        del sequence[index]
        
    #print(repeat, len(repeat))
    #Start the process
    stepper = 0
    copy_section = []
    copy_durations = []
    repeat_times = 0
    control_loop = 0
    repeat_bar = 0
    
    #r_id = 0
    repeat_done = False
    done = True
    this_repeat = None
    next_repeat = None
    
    while done:
        #grab the element 
        e = sequence[stepper]
        d = duration_sequence[stepper]
        #print(stepper, e)
        if e == '|:':
            form_zone['start'] = stepper  
        
        if e.startswith('Repeat') and repeat_done == False:
            #find the repeat that is located in that stepper
            for current in repeat:
            # Check if the 'loc' value of the current dictionary matches the stepper value
                if current['loc'] == stepper:
                    # If it matches, store the dictionary and break the loop
                    this_repeat = current
                    this_id = current['id']
                    break 
            #Ask if this repeat is done
            if this_repeat['done'] == False:
                inner_zone['start'] = stepper 
                id = this_repeat['id']   
                if verbose: print('first repeat done', stepper, id)           
                #move forward
                stepper += 1
                e = sequence[stepper]
                d = duration_sequence[stepper]
                repeat[id]['done'] = True
                
                #Ask which is the next available repeat? 
                for current in repeat:
                    if current['done'] == False:
                        next_repeat = current
                        if verbose: print('next repeat:', next_repeat['loc'], next_repeat['id'])
                        break
                if (next_repeat == None):
                    if verbose: print('All repetitions done 0')
                    done = False
                    break
            
            elif this_repeat['done'] == True and next_repeat['done'] == False and repeat[this_id]['id'] < len(repeat)-1:
                #jump to the next repeat jumping ':|', '|' and 'Repeat_'
                next_loc = next_repeat['loc'] + 1
                stepper = next_loc
                e = sequence[stepper]
                d = duration_sequence[stepper]
                
                id_next = next_repeat['id']
                repeat[id_next]['done'] = True
                if verbose: print('second repeat done at', 'stepper:', stepper, 'id:', id)
                
            elif repeat[repeat_times]['done'] == True and repeat[this_id]['id'] == len(repeat)-1:
                #repeat_done = True
                #TODO: check if this section is needed
                if verbose: print('All repetitions done')
                #done = False #close the loop
                #e = 'None'
            
        
        if e == ':|':
            current = close[repeat_bar]
            #check the current repetition turn
            if current['done'] == True and repeat_bar < len(close)-1:
                repeat_bar += 1
                current = close[repeat_bar]
                #print('next close repetition')
            
            #do the repetition    
            if current['done'] == False:
                
                #save location 
                form_zone['end'] = stepper
                inner_zone['end'] = stepper
                
                #move to the original location
                stepper = form_zone['start'] + 1
                e = sequence[stepper]
                d = duration_sequence[stepper]
                
                #update its information
                close[repeat_bar]['done'] = True  
                current['done'] = True    
                #print('repetition done', repeat_bar)
        
        #copy the information    
        copy_section.append(e)
        copy_durations.append(d)
        
        stepper += 1
        control_loop += 1
        if stepper == len(sequence):
            done = False
        if control_loop > 3000:
            print('ERROR: -----> Control loop break! \nid:', id)
            status = False
            return 0, 0, status
    
    copy_section = intro_data + copy_section
    copy_durations = np.insert(copy_durations, 0, [0, 0])
    
    copy_section = [x.replace(':|', '|') for x in copy_section]
    copy_section = [x.replace('|:', '|') for x in copy_section]
    
    if verbose: 
        print('Process completed successfully..', 'New form length:', len(copy_section))
        print("-----------------------------\n")
    return copy_section, copy_durations, status 

#----------------------------------------------------------------------------------
def formatChordsVocabulary(theChordsSequence, theOffetsSequence, blockSize):
    chord_sequence_list = []
    duration_sequence_list = []
    i = 0
    for theChords, theOffets in zip(theChordsSequence, theOffetsSequence):
        theChords = np.array(theChords, dtype=object)
        theOffets = np.array(theOffets, dtype=float)
        
        #divide the chords into sections base, nature, extension, slash
        #the first two elements are the style 
        the_sequence = theChords[2:]
        the_duration = theOffets[2:]

        format = theChords[0:2].tolist()
        duration_format = theOffets[0:2].tolist()

        the_sequence, the_duration = getArrayOfElementsInChord(the_sequence, the_duration)
        the_duration = duration_format + the_duration
        the_sequence = format + the_sequence

        #the final format of the sequence is:
        the_sequence = format_start_end(the_sequence)
        the_duration = format_start_end(the_duration)
        
        #if (the_sequence.shape[0] > 768):
        #    print(i, the_sequence.shape[0], the_duration.shape[0], format)
        
        the_sequence = padding(the_sequence, blockSize)
        the_duration = padding(the_duration, blockSize)
        
        chord_sequence_list.append(the_sequence)
        duration_sequence_list.append(the_duration)
        i+=1
            
    chord_sequence_list = np.array(chord_sequence_list, dtype=object)
    duration_sequence_list = np.array(duration_sequence_list, dtype=object)
    print(chord_sequence_list.shape, duration_sequence_list.shape)
    return chord_sequence_list, duration_sequence_list

#----------------------------------------------------------------------------------
def correctDuplicatedExtensions(dataset, duration):
    corrected_datset = []
    corrected_duration = []
    #i = 0
    for song, off in zip(dataset, duration):
        cleaned_list = []
        cleanned_duration = []
        for chord, ofNum in zip(song, off):
            new = []
            s = chord.split(' ')
            if len(s) >= 2 and len(s) % 2 == 0:
                tmp = s[0] + ' ' + s[1]
                new.append(tmp)
                for i in range(2, len(s), 2):
                    r = s[i]+ ' ' + s[i+1]
                    if tmp != r:
                        new.append(r)
                        
            else:
                new.append(chord)
            
            new = ' '.join(new)
            cleaned_list.append(new)
            cleanned_duration.append(ofNum)
        #i+=1
        corrected_datset.append(cleaned_list)
        corrected_duration.append(cleanned_duration)
    corrected_datset = np.array(corrected_datset, dtype=object)
    corrected_duration = np.array(corrected_duration, dtype=object)
    print(corrected_datset.shape, corrected_duration.shape)
    return corrected_datset, corrected_duration

