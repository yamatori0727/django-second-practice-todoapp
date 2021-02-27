from django.db import models

# タプルの右側が、選択式で表示される名前。左が格納される名前、機械が読み込む名前。
CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=100,
        choices=CHOICE  # choices=で、選択式にできる。
    )
    duedate = models.DateField()

    # オブジェクトが作成された際に実行される関数。文字列情報を返す。
    def __str__(self):
        return self.title
