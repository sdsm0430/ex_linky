from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from linky.models import Musical, Script
import csv, os

@receiver(post_save, sender=Musical)
def renew_scripts(sender, **kwargs):
    musical = kwargs['instance']
    if(musical.csv):
        # 먼저 script 잡고 다 지움
        scrts = Script.objects.filter(musical=musical)
        for scr in scrts:
            scr.delete()
        # 이제 저장
        with open(os.path.join(settings.BASE_DIR, os.path.join(settings.MEDIA_ROOT, musical.csv.name)), 'r') as f:
            rd = csv.reader(f)
            for line in rd:
                try:
                    idx, lang, song, actor, text = line
                    if(idx == "순서"):  # 가장 위의 index일 때
                        continue
                    else:
                        Script.objects.create(musical=musical, language=lang,
                                              order=idx, music=song, actor=actor, song=text)
                except:  # 잘못된 line
                    print("잘못되었습니다")

    else:
        # csv가 없을 때 do nothing
        pass
