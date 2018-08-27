from datetime import date
from random import randint

from zeep.plugins import HistoryPlugin

from fastems import Services
from fastems.job import job_factory
from fastems.order import PlannedOrder


def create_order():

    job_data = {
        'part_number': 'HB96-15',
        'description': 'Fastems Bridge Order Creation Test',
        'order_number': 99999,
        'qty': randint(10000, 90000),
        'due_date': date(2018, 8, 29)
    }

    job = job_factory(**job_data)
    work_order = PlannedOrder(job)

    # print(work_order.__dict__)

    try:
        response = work_order.submit()

        print(response)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    history = HistoryPlugin()
    client = Services.Order
    client.plugins.append(history)

    orders = client.service.GetOrders({
        'ids': [
            "0d20da0c-501a-43dc-a250-a74b008ca926"
        ]
    })

    print(history.last_sent['envelope'])
    print(history.last_received['envelope'])
    print(orders)
