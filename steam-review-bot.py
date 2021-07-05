# Reference: https://pypi.org/project/steamreviews/

import steamreviews

def steamReviews():
    request_params = dict()
    request_params['language'] = 'english'

    app_id = 275850 # Steam ID for No Man's Sky
    review_dict, query_count = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params=request_params)

if __name__ == '__main__':
    steamReviews()
