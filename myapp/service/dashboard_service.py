from myapp.buisness import dashboard_bll
def get_dashboard_data():
    dashboard_data = {}

    dashboard_data.update(dashboard_bll.get_dashboard_status())
    return dashboard_data

