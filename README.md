# Visual_slam_test_issue
This is repository for visual slam test issue

## Результаты

1) задание

получилось запустить openvslam и получить результат для видео 20240327_161347_448.mp4 (все работает при запуске через docker run, но через docker-comopse пока еще падает, почтараюст починить, там проблема с окружением и прокидыванием дисплея в контейнер)

Сейчас пытаюсь сделать так, чтобы запустилось в Kiemera-VIO, но пока не получилось переделать видео под формат датасета [EUROC](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets)
Если будет еще время постараюсь как-то завести

2) задание

Из результата построил обпако точек ```result.csv``` и для визулизации на основе plotly отрисовал облако (получилось как-то не понятно, по хорошему надо разобраться)

3) задание

Пока не разбирался с данными сенсров, так как оно должно будет много времени отнять (работал не все выходные, примерно часов 5-6)


## Upd

Построил траектории, но они получились странные, заетил, что траектории и лэндмарки маппинга странные, пока не разобрался можно ли менять массштаб при маппинге и локализации

Перед запуском скриптов надо собрать конейтнер openvslam-1

Для запуска сначала нужно вызвать
```
bash pre_run.sh
```

Далее поместить видео датасет в папку dataset и запустить:
- для маппинга ```bash openvslam_mapping.sh```
- для локализации ```openvslam_localization.sh```
