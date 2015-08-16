import sys
from datetime import datetime, date, timedelta
from exercises.models import *

# edit this start date to adjust start date for all experiments
target_start_date = date(2015, 7, 13)


# clear old data:
PhaseSection.objects.all().delete()


ps = []

ps.append(PhaseSection(phase='phase1', section='pretest',start_date = target_start_date + timedelta(weeks = 0)))
ps.append(PhaseSection(phase='phase1', section='training',start_date = target_start_date + timedelta(weeks = 0)))
ps.append(PhaseSection(phase='phase1', section='posttest1',start_date = target_start_date + timedelta(weeks = 2)))
ps.append(PhaseSection(phase='phase1', section='posttest2',start_date = target_start_date + timedelta(weeks = 4)))
ps.append(PhaseSection(phase='phase1', section='posttest3',start_date = target_start_date + timedelta(weeks = 8)))

ps.append(PhaseSection(phase='phase2', section='pretest',start_date = target_start_date + timedelta(weeks = 8)))
ps.append(PhaseSection(phase='phase2', section='training',start_date = target_start_date + timedelta(weeks = 8)))
ps.append(PhaseSection(phase='phase2', section='posttest1',start_date = target_start_date + timedelta(weeks = 10)))
ps.append(PhaseSection(phase='phase2', section='posttest2',start_date = target_start_date + timedelta(weeks = 12)))
ps.append(PhaseSection(phase='phase2', section='posttest3',start_date = target_start_date + timedelta(weeks = 16)))

ps.append(PhaseSection(phase='phase3', section='pretest',start_date = target_start_date + timedelta(weeks = 16)))
ps.append(PhaseSection(phase='phase3', section='training',start_date = target_start_date + timedelta(weeks = 16)))
ps.append(PhaseSection(phase='phase3', section='posttest1',start_date = target_start_date + timedelta(weeks = 18)))
ps.append(PhaseSection(phase='phase3', section='posttest2',start_date = target_start_date + timedelta(weeks = 20)))
ps.append(PhaseSection(phase='phase3', section='posttest3',start_date = target_start_date + timedelta(weeks = 24)))






for i in ps:
  i.save()

