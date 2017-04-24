def lambda_handler(event, context):
    print(
        'Search was running with the following parameters - {0} \n'
        'Regions - {1} \n'
        'Resource types - {2}'.format(tagsChecker, regions, resource_types)
        )
