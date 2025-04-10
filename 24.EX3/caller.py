import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import necessary Django ORM tools
from django.db.models import Count, Sum, F, Avg
from main_app.models import Astronaut, Mission, Spacecraft


def get_last_completed_mission():
    """
    Retrieves the last completed mission based on launch date.
    Returns details including commander, astronauts, spacecraft, and total spacewalks.
    """
    last_mission = Mission.objects.filter(status="Completed").order_by('-launch_date').first()

    if not last_mission:
        return "No data."

    commander_name = last_mission.commander.name if last_mission.commander else "TBA"
    astronaut_names = last_mission.astronauts.order_by('name').values_list('name', flat=True)
    spacecraft_name = last_mission.spacecraft.name
    total_spacewalks = last_mission.astronauts.aggregate(total_spacewalks=Sum('spacewalks'))['total_spacewalks'] or 0

    return f"The last completed mission is: {last_mission.name}. " \
           f"Commander: {commander_name}. " \
           f"Astronauts: {', '.join(astronaut_names)}. " \
           f"Spacecraft: {spacecraft_name}. " \
           f"Total spacewalks: {total_spacewalks}."


def get_most_used_spacecraft():
    """
    Retrieves the spacecraft that has been used in the most missions.
    Orders by number of missions descending, then by name ascending.
    """
    spacecraft = Spacecraft.objects.annotate(
        mission_count=Count('missions'),
        unique_astronauts=Count('missions__astronauts', distinct=True)
    ).order_by('-mission_count', 'name').first()

    if not spacecraft or spacecraft.mission_count == 0:
        return "No data."

    return f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, " \
           f"used in {spacecraft.mission_count} missions, astronauts on missions: {spacecraft.unique_astronauts}."


def decrease_spacecrafts_weight():
    """
    Decreases weight of spacecrafts assigned to planned missions by 200kg,
    ensuring weight doesn't drop below 0.0.
    Returns count of updated spacecrafts and new average weight.
    """
    spacecrafts = Spacecraft.objects.filter(
        missions__status="Planned",
        weight__gte=200.0
    ).distinct()

    affected_count = spacecrafts.update(weight=F('weight') - 200.0)

    if affected_count == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']
    return f"The weight of {affected_count} spacecrafts has been decreased. " \
           f"The new average weight of all spacecrafts is {avg_weight:.1f}kg."
