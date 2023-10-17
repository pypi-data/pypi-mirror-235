# orchestrator.py

import time
import datetime as dt
from multiprocessing import Process
from typing import Iterable, Dict, Any, Optional, Union, Type, List

from looperator import Operator, Superator

from socketsio import Server, BCP, TCP, Client, find_available_port

from crypto_screening.screeners.container import ScreenersContainer
from crypto_screening.screeners.combined import (
    combined_market_screener, CategoryBase, Categories
)
from crypto_screening.screeners.orchestration.method import (
    OrchestrationMethod
)
from crypto_screening.screeners.collectors import (
    SocketScreenersDataCollector
)
from crypto_screening.screeners.callbacks import SocketCallback
from crypto_screening.screeners.orchestration.publisher import (
    DataPublisher
)
from crypto_screening.screeners.orchestration.controller import (
    DataPublisherController
)

__all__ = [
    "DataPublisherClient",
    "DataPublisherServer",
    "Orchestrator",
    "create_run_data_publisher_server",
    "data_publisher_server"
]

class DataPublisherClient(DataPublisherController):
    """A server to run the data publisher on."""

    def __init__(self, client: Client, process: Optional[Process] = None) -> None:
        """
        Defines the attributes of the controller client.

        :param client: The client object.
        :param process: The process to control.
        """

        super().__init__()

        self.client = client
        self.process = process
    # end __init__
# end DataPublisherServer

class DataPublisherServer(Superator):
    """A server to run the data publisher on."""

    def __init__(self, publisher: DataPublisher, server: Server) -> None:
        """
        Defines the attributes of the data publisher server.

        :param publisher: The data publisher object.
        :param server: The control server object.
        """

        self.publisher = publisher
        self.server = server

        self._operator = Operator(
            operation=lambda: (
                server.handle(
                    action=self.publisher.commit,
                    sequential=True
                )
            ),
            termination=lambda: (
                self.publisher.market.stop(),
                self.publisher.callback.stop()
            )
        )

        super().__init__(operators=[self._operator])
    # end __init__
# end DataPublisherServer

def create_run_data_publisher_server(
        control_address: str,
        control_port: int,
        data_address: str,
        data_port: int,
        parameters: Dict[str, Any]
) -> None:
    """
    Creates the market screener object for the data.

    :param control_address: The address for the control server.
    :param control_port: The port for the control server.
    :param data_address: The address for the data server.
    :param data_port: The port for the data server.
    :param parameters: The parameters for the market screener.

    :return: The data publisher server object.
    """

    service = data_publisher_server(
        control_address=control_address,
        control_port=control_port,
        data_address=data_address,
        data_port=data_port,
        parameters=parameters
    )
    service.server.listen()
    service.run(block=True)
# end create_run_data_publisher_server

def data_publisher_server(
        control_address: str,
        control_port: int,
        data_address: str,
        data_port: int,
        parameters: Dict[str, Any]
) -> DataPublisherServer:
    """
    Creates the market screener object for the data.

    :param control_address: The address for the control server.
    :param control_port: The port for the control server.
    :param data_address: The address for the data server.
    :param data_port: The port for the data server.
    :param parameters: The parameters for the market screener.

    :return: The data publisher server object.
    """

    server = Server(BCP(TCP()))
    server.bind((control_address, control_port))

    callback = SocketCallback(address=data_address, port=data_port)

    market = combined_market_screener(**parameters, callbacks=[callback])

    publisher = DataPublisher(market=market, callback=callback)

    return DataPublisherServer(publisher=publisher, server=server)
# end data_publisher_server

Data = Dict[str, Iterable[Union[str, Dict[str, Iterable[str]]]]]
Collectors = Dict[
    SocketScreenersDataCollector,
    List[DataPublisherClient]
]

class Orchestrator:
    """A class to represent an orchestrator of market screeners."""

    def __init__(self, collectors: Optional[Collectors] = None) -> None:
        """
        Defines the connection attributes of the orchestrator.

        :param collectors: The collectors to run.
        """

        if collectors is None:
            collectors = {}
        # end if

        self.collectors: Collectors = collectors
    # end __init__

    def create(
            self,
            data: Union[Data, Dict[Type[CategoryBase], Data]],
            method: OrchestrationMethod,
            address: Optional[str] = None,
            port: Optional[int] = None,
            categories: Optional[Type[CategoryBase]] = None,
            cancel: Optional[Union[float, dt.timedelta]] = None,
            delay: Optional[Union[float, dt.timedelta]] = None,
            limited: Optional[bool] = None,
            amount: Optional[int] = None,
            memory: Optional[int] = None,
            location: Optional[str] = None,
            refresh: Optional[Union[float, dt.timedelta, bool]] = None,
            control_address: Optional[str] = None
    ) -> None:
        """
        Creates the market screener object for the data.

        :param data: The market data.
        :param method: The orchestration method.
        :param categories: The categories for the markets.
        :param limited: The value to limit the screeners to active only.
        :param refresh: The refresh time for rerunning.
        :param amount: The maximum amount of symbols for each feed.
        :param location: The saving location for the data.
        :param delay: The delay for the process.
        :param cancel: The cancel time for the loops.
        :param memory: The memory limitation of the market dataset.
        :param control_address: The address for the control server.
        :param address: The address for the data server.
        :param port: The port for the data server.

        :return: The data publisher server object.
        """

        screeners = combined_market_screener(
            data=data, location=location,
            memory=memory, categories=categories
        ).screeners

        if address is None:
            address = "127.0.0.1"
        # end if

        if port is None:
            port = find_available_port(address)
        # end if

        collector = SocketScreenersDataCollector(
            address=address, port=port, screeners=screeners
        )

        self.add(
            collector=collector,
            method=method,
            cancel=cancel,
            delay=delay,
            limited=limited,
            amount=amount,
            refresh=refresh,
            control_address=control_address
        )
    # end create

    def add(
            self,
            collector: SocketScreenersDataCollector,
            method: OrchestrationMethod,
            cancel: Optional[Union[float, dt.timedelta]] = None,
            delay: Optional[Union[float, dt.timedelta]] = None,
            limited: Optional[bool] = None,
            amount: Optional[int] = None,
            refresh: Optional[Union[float, dt.timedelta, bool]] = None,
            control_address: Optional[str] = None
    ) -> List[DataPublisherClient]:
        """
        Creates the market screener object for the data.

        :param collector: The collector to create a process for.
        :param method: The orchestration method.
        :param limited: The value to limit the screeners to active only.
        :param refresh: The refresh time for rerunning.
        :param amount: The maximum amount of symbols for each feed.
        :param delay: The delay for the process.
        :param cancel: The cancel time for the loops.
        :param control_address: The address for the control server.

        :return: The data publisher server object.
        """

        if control_address is None:
            control_address = "127.0.0.1"
        # end if

        data = {}

        for category in Categories.categories:
            screeners = collector.find_screeners(
                base=category.screener
            )

            if screeners:
                container = ScreenersContainer(screeners=screeners)
                data[category] = (
                    container.map()
                    if container is Categories.ohlcv else
                    container.structure()
                )
            # end if
        # end for

        processes = []

        create = lambda d, c: Process(
            target=create_run_data_publisher_server,
            kwargs=dict(
                control_address=control_address,
                control_port=c,
                data_address=collector.address,
                data_port=collector.port,
                parameters=dict(
                    data=d,
                    cancel=cancel,
                    delay=delay,
                    limited=limited,
                    amount=amount,
                    memory=1,
                    refresh=refresh
                )
            )
        )

        if method == OrchestrationMethod.ALL:
            port = find_available_port(control_address)
            process = create(data, port)

            processes.append((process, port))

            process.start()

        elif method == OrchestrationMethod.CATEGORIES:
            for category, category_data in data.items():
                port = find_available_port(control_address)
                process = create(
                    {category: category_data},
                    port
                )

                processes.append((process, port))

                process.start()
            # end for

        elif method == OrchestrationMethod.EXCHANGES:
            for category, category_data in data.items():
                for exchange, exchange_data in category_data.items():
                    port = find_available_port(control_address)
                    process = create(
                        {category: {exchange: exchange_data}},
                        port
                    )

                    processes.append((process, port))

                    process.start()
                # end for
            # end for

        elif method == OrchestrationMethod.INDIVIDUALS:
            for category, category_data in data.items():
                for exchange, exchange_data in category_data.items():
                    for symbol in exchange_data:
                        port = find_available_port(control_address)
                        # noinspection PyTypeChecker
                        process = create(
                            {
                                category: {
                                    exchange: (
                                        {symbol} if
                                        not isinstance(exchange_data, dict) else
                                        {symbol: exchange_data[symbol]}
                                    )
                                }
                            }, port
                        )

                        processes.append((process, port))

                        process.start()
                    # end for
                # end for
            # end for
        # end if

        for process, port in processes:
            client = Client(BCP(TCP()))

            count = 0

            while not client.connected:
                try:
                    client.connect((control_address, port))

                except ConnectionError as e:
                    if count == 5:
                        raise e
                    # end if

                    time.sleep(1)

                    count += 1
                # end try
            # end while

            controller = DataPublisherClient(client=client, process=process)

            self.collectors.setdefault(collector, []).append(controller)
        # end for

        return list(self.collectors[collector])
    # end add

    def start_screening(self) -> None:
        """Starts collecting the data."""

        for controllers in self.collectors.values():
            for controller in controllers:
                if controller.process and controller.process.is_alive():
                    controller.client.send(controller.run())
                    print(controller.receive(controller.client.receive()[0]))
                # end if
            # end for
        # end for
    # end start_screening

    def stop_screening(self) -> None:
        """Starts collecting the data."""

        for controllers in self.collectors.values():
            for controller in controllers:
                if controller.process and controller.process.is_alive():
                    controller.client.send(controller.stop())
                # end if
            # end for
        # end for
    # end stop_screening

    def terminate(self) -> None:
        """Starts collecting the data."""

        self.stop_screening()

        for controllers in self.collectors.values():
            for controller in controllers:
                if controller.process and controller.process.is_alive():
                    controller.process.terminate()
                # end if
            # end for
        # end for
    # end terminate

    def start_collecting(self) -> None:
        """Starts collecting the data."""

        for collector in self.collectors:
            if not collector.screening:
                collector.start_screening()
            # end if
        # end for
    # end start_collecting

    def stop_collecting(self) -> None:
        """Starts collecting the data."""

        for collector in self.collectors:
            if not collector.screening:
                collector.stop_screening()
            # end if
        # end for
    # end stop_collecting
# end Orchestrator