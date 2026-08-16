# Produced healthcare suggestions according to identified patient risk factors and health conditions.
# The generate_recommendations and get_recommendations functions are called to generate unique care suggestions and return results.

# Generating patient recommendations
def generate_recommendations(factors):


    # Creating recommendation list
    recommendations = []



    # Checking blood pressure risk
    if "High Blood Pressure" in factors:


        # Adding blood pressure monitoring guidance
        recommendations.append(

            "Monitor blood pressure regularly"

        )


        # Adding heart healthy diet guidance
        recommendations.append(

            "Reduce sodium intake and maintain a heart healthy diet"

        )


        # Adding healthcare guidance
        recommendations.append(

            "Consult healthcare provider for blood pressure management"

        )



    # Checking blood sugar risk
    if "High Blood Sugar" in factors:


        # Adding glucose monitoring guidance
        recommendations.append(

            "Monitor blood glucose levels regularly"

        )


        # Adding diabetes care guidance
        recommendations.append(

            "Maintain diabetic care plan"

        )


        # Adding nutrition guidance
        recommendations.append(

            "Reduce sugar intake and follow balanced nutrition"

        )



    # Checking smoking risk
    if "Smoking History" in factors:


        # Adding smoking support guidance
        recommendations.append(

            "Consider smoking cessation program"

        )


        # Adding tobacco avoidance guidance
        recommendations.append(

            "Avoid tobacco exposure to reduce cardiovascular risk"

        )



    # Checking BMI risk
    if "High BMI" in factors:


        # Adding fitness guidance
        recommendations.append(

            "Follow healthy diet and regular exercise plan"

        )


        # Adding weight management guidance
        recommendations.append(

            "Maintain healthy body weight"

        )



    # Checking oxygen risk
    if "Low Oxygen Level" in factors:


        # Adding respiratory guidance
        recommendations.append(

            "Evaluate respiratory condition"

        )


        # Adding emergency guidance
        recommendations.append(

            "Seek medical attention if breathing difficulty occurs"

        )



    # Checking age risk
    if "Advanced Age" in factors:


        # Adding checkup guidance
        recommendations.append(

            "Schedule regular healthcare checkups"

        )


        # Adding vital monitoring guidance
        recommendations.append(

            "Monitor vital signs regularly"

        )



    # Checking heart rate risk
    if "High Heart Rate" in factors:


        # Adding heart rate guidance
        recommendations.append(

            "Monitor heart rate regularly"

        )


        # Adding stress management guidance
        recommendations.append(

            "Avoid excessive physical stress until evaluated"

        )



    # Checking diabetes risk
    if "Diabetes" in factors:


        # Adding diabetes management guidance
        recommendations.append(

            "Maintain diabetes medication and lifestyle plan"

        )



    # Removing duplicate recommendations
    recommendations = list(

        dict.fromkeys(recommendations)

    )



    # Checking empty recommendation list
    if len(recommendations) == 0:


        # Adding healthy lifestyle guidance
        recommendations.append(

            "Continue current healthy lifestyle"

        )



    # Returning recommendations
    return recommendations





# Providing recommendation API function
def get_recommendations(factors):


    # Returning generated recommendations
    return generate_recommendations(factors)