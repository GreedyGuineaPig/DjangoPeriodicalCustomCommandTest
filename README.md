# DjangoPeriodicalCustomCommandTest

Djanogoでカスタムコマンドを作成し、定期的に実行します。

バッチ起動コマンド
python manage.py batch

サーバー起動コマンド
python manage.py runserver

カスタムコマンドは任意のapp内の　/management/commands/　に格納します。

任意のコマンドを定期実行するにはAPSchedulerを使用します。（testApp内）
Djangoの仕様上複数のプロセスが並行して走るため、定期実行されるコマンドは２回以上実行されることがあります。
なので、ap_scheduler.py で同一処理がすでにスケジュールに登録されていないか確認する処理を行いました。
