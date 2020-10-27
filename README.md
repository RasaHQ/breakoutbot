<img src="logo.png" width=200 align="right">

# BreakoutBot

This repository contains an example project of a text-based adventure game built with Rasa. The
goal is to host and maintain a proper text based escape room that you can play with. This project
is open to outside contributions and we're recording the milestones/lessons learned in a series
on Youtube.

## Youtube

You can find the Youtube playlist for this repository [here](https://www.youtube.com/playlist?list=PL75e0qA87dlGS2ik6n1sN-KjG39yCrGgf).

## Contributing

There are many ways you can contribute to this project.

- **Give feedback.** If you play with the assistant and notice that there are features missing we'd love to hear it.
- **Add data.** If you think that there's data missing for some intents you're free to create a PR.
- **Think along.** There are tricky parts to making a proper adventure game in Rasa and we're still learning as we go.
  Feel free to join some of the discussions in the issues to think along.
- **Report bugs.** If you feel like some of the commands make no sense, feel free to let us know!

If your issue is Rasa related, you might be able to find help on our [forum](https://forum.rasa.com).

## Start Locally

If you want to play around with this game locally you can clone this repository and setup Rasa. This project currently uses Rasa version 1.10.

```
git clone git@github.com:RasaHQ/breakoutbot.git
pip install rasa==1.10
rasa train
```

Once you've done this, you should be able to run rasa actions and play the game.

```python
rasa run actions & rasa shell
```

If you want to run this with Rasa X locally, you'll need to install it first.

```python
python -m pip install rasa-x==0.31 -i https://pypi.rasa.com/simple
rasa x
```

Remember, when you're running Rasa X you'll also need to make sure that the custom actions are running in the background.

## Versions

On our youtube channel we've started a small documentary on the development of this text-based adventure game. Depending on what videos you're watching we might have a different version of Rasa in the running version of this project. In the overview below you can confirm what versions we've used and you can also find the reference to the saved code in case you want to re-run the code.

| Season 	      | Youtube Link 	                                                                                                                        | Rasa Version 	| Rasa X Version | Code Link 	                                                  |
|-------------	|-------------------------------------------------------------------------------------------------------------------------------------	|--------------	| -------------- |------------------------------------------------------------	|
| Season One  	| [Link](https://www.youtube.com/watch?v=rzTSSSnNOpA&list=PL75e0qA87dlGS2ik6n1sN-KjG39yCrGgf&index=2&t=0s&ab_channel=Rasa)             	| 1.10        	|             	 | [S1](https://github.com/RasaHQ/breakoutbot/releases/tag/s1)  |
| Season Two  	| [Link](https://www.youtube.com/watch?v=0d_gF4GP7VU&list=PL75e0qA87dlGS2ik6n1sN-KjG39yCrGgf&index=8&ab_channel=Rasa)             	    | 1.10        	| 0.31           | [S2](https://github.com/RasaHQ/breakoutbot/releases/tag/s2)  |
| Season Three  | [Link](https://www.youtube.com/watch?v=QatqgIR09xY&list=PL75e0qA87dlGS2ik6n1sN-KjG39yCrGgf&index=15)             	    | 1.10        	| 0.31           | [S3](https://github.com/RasaHQ/breakoutbot/releases/tag/s3)  |
