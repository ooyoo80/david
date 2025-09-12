## 반달곰 커피 홈페이지

[반달곰 커피](https://반달곰커피)



오디오 출력 소스코드
```python
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
```


![david]([[https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mfab.hu%2Fartworks%2F18749%2F&psig=AOvVaw11Chx-NzdPAGe_D_vL1A5X&ust=1757749392200000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCICfkb7d0o8DFQAAAAAdAAAAABA](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mfab.hu%2Fartworks%2F18749%2F&psig=AOvVaw11Chx-NzdPAGe_D_vL1A5X&ust=1757749392200000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCICfkb7d0o8DFQAAAAAdAAAAABAE)](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mfab.hu%2Fartworks%2F18749%2F&psig=AOvVaw11Chx-NzdPAGe_D_vL1A5X&ust=1757749392200000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCICfkb7d0o8DFQAAAAAdAAAAABAE))
