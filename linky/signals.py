from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from linky.models import Musical, Script
import csv, os
from django.db import transaction

@transaction.atomic
@receiver(post_save, sender=Musical)
def renew_scripts(sender, **kwargs):
    musical = kwargs['instance']
    if(musical.csv):
        scrts = Script.objects.filter(musical=musical)
        for scr in scrts:
            scr.delete()
        with open(os.path.join(settings.BASE_DIR, os.path.join(settings.MEDIA_ROOT, musical.csv.name)), 'r') as f:
            rd = csv.reader(f)
            for line in rd:
                idx, lang, song, actor, text = line
                if(idx == "idx"):  # 가장 위의 index일 때
                    continue
                else:
                    Script.objects.create(musical=musical, language=lang,
                     order=idx, music=song, actor=actor, song=text)

    else:
        # csv가 없을 때 do nothing
        pass
