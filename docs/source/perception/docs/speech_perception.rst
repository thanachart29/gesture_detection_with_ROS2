.. _speech_perception:

Speech Perception
#####################

.. raw:: html

    <h1 align="center">
      <div>
        <div style="position: relative; padding-bottom: 0%; overflow: hidden; max-width: 100%; height: auto;">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/4H2NkHMDs6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
      </div>
    </h1>

Overview
**********
pakage that build on ros2 foxy for caoco robot to recognize, synthesis speech and keyword finding

Architecture
""""""""""""""

.. image:: ./images/Speech_architecture.png
    :width: 480
    :align: center

|

Concept
""""""""
we have 2 node 1 for process algorithm and 1 for interface

- Node speech process

    It will receive command from speechInterface and process it the main function are

    - callSpeak : It will call speak function to play sound file that already synthesized from gtts if it can not find the file it will use pyttsx3 to synthesis the sound

    .. code-block:: python

        def callSpeak(self, msg):
        #try to find the file in the path and play it
            try:
                playsound(self.path + msg + '.mp3')
            except:
                self.get_logger().info('can not find the file')
                self.engine.say(msg)
                self.engine.runAndWait()
    
    - listen : It will listen to microphone and convert it to text by using sphinx and speech recognition and return the text

    .. code-block:: python

        def listen(self):
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout = self.timeout, phrase_time_limit = self.phrase_time_limit)
                    text = r.recognize_sphinx(audio)
                    self.get_logger().info('I hear: %s' % text)
                    if(text == ''):
                        text = 'Empty string'
                    text.lower()
                    return text
            except sr.UnknownValueError:
                self.get_logger().info('I can not hear')
                return ''
            except sr.RequestError as e:
                self.get_logger().info('I can not hear')
                return ''

    - timer callback: It will check if there is command to enable each ability and if there have command it will start to publish data

    .. code-block:: python

        def timer_callback(self):
            if(self.first_time_finish == True):
                self.first_time_finish = False
                self.isEnable_finish = True
                self.FinishFunction()
            elif(self.first_time_bag == True):
                self.first_time_bag = False
                self.isEnable_bag = True
                self.BagFunction()
            elif(self.first_time_start == True):
                self.first_time_start = False
                self.isEnable_start = True
                self.StartFunction()
            elif(self.first_time_end == True):
                self.first_time_end = False
                self.isEnable_end = True
                self.EndFunction()



- Node speechInterface

    It will be service server to receive command and adjust parameter of node speechprocess and it will be publisher to send status of each ability

    .. code-block:: python

        def speech2TextBagCallback(self, request, response):
            self.control.first_time_bag = True
            return response
        def publish(self):
            if(self.control.isEnable_bag):
                self.pub_speech2textBag.publish(self.control.param_status_bag)
            ....
            if(self.control.param_status_bag.data != 0):
                self.control.isEnable_bag = False
                self.pub_speech2textBag.publish(self.control.param_status_bag)
                self.control.param_status_bag.data = 0


Installation
*************

Python library
""""""""""""""""

- playsound

    .. code-block:: bash

        pip install SpeechRecognition

- speech recognition

    .. code-block:: bash

        pip install SpeechRecognition

- sphinx

    .. code-block:: bash

        pip install pocketsphinx

- pyttsx3

    .. code-block:: bash

        pip install pyttsx3

- gtts

    .. code-block:: bash

        pip install gtts

- pyaudio

    .. code-block:: bash

        pip install pyaudio

Example
*********

1. clone GitHub repository from

    .. code-block:: bash

        git clone https://github.com/MBSE-2022-1/Software-Team.git -b speech perception

2. Open terminal and run following command

    .. code-block:: bash

        colcon build
        source install/setup.bash

    .. note:: Don't build with symlink-install

3. Run command

    .. code-block:: bash

        ros2 run speech speech.py

4. Open new terminal and run command

    .. code-block:: bash

        ros2 service call /speech2text_start/enable std_srvs/srv/Empty


.. API Reference
.. ***************


Subsystem Verification
************************

speech detection with noise cancellation
""""""""""""""""""""""""""""""""""""""""""""
can ignore a noise and still recognize the word that we want in situation that there have a person talk in the same room  we adding sound form video people talking

- result

.. image:: ./images/Speech_result.png
    :width: 480
    :align: center

|

    the result will show that it can detect the word that we want but it also detect the noise that we don't want

    model speech recognition have low accuaracy it often go wrong word.


Problem and future plan
*************************

**Future Plan**

training model for speech recognition to improve accuracy and speed of recognition and use machine learning to know what the user want to do
