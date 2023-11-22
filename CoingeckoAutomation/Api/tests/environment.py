def before_scenario(context, scenario):
    context.url = 'https://api.coingecko.com/api/v3/'


def after_scenario(context, scenario):
    print('Finishing')
