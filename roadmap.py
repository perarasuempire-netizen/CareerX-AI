def generate_roadmap(target_role, missing_skills):

    roadmap = []

    if not missing_skills:
        roadmap.append(
            "You already have most of the required skills."
        )
        return roadmap

    for week, skill in enumerate(missing_skills, start=1):

        roadmap.append(
            f"Week {week}: Learn {skill.title()}"
        )

    return roadmap