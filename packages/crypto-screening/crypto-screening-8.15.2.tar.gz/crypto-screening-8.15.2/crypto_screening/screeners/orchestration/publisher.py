# publisher.py

import json
import socket
from typing import Tuple

from represent import represent

from looperator import Handler, Operator, Superator

from socketsio import BaseProtocol

from crypto_screening.screeners.recorder import MarketScreener
from crypto_screening.screeners.callbacks import SocketCallback
from crypto_screening.screeners.orchestration.requests import (
    load_request, UpdateRequest, RunRequest, StopRequest,
    UnpauseRequest, PauseRequest, ServiceRequest, ConfigRequest
)
from crypto_screening.screeners.orchestration.responses import (
    JSONErrorResponse, ServiceResponse, DataErrorResponse,
    UpdateSuccessResponse, RunSuccessResponse, ConfigResponse,
    PauseSuccessResponse, UnpauseSuccessResponse,
    RequestErrorResponse, StopSuccessResponse
)

__all__ = [
    "DataPublisher"
]


Connection = socket.socket
Address = Tuple[str, int]

@represent
class DataPublisher(Superator):
    """A class to represent arbitrage events sending server."""

    def __init__(
            self,
            market: MarketScreener,
            callback: SocketCallback
    ) -> None:
        """
        Defines the attributes of the arbitrage sender.

        :param market: The market screener object.
        :param callback: The sockets callback object.
        """

        super().__init__([])

        self.market = market
        self.callback = callback
    # end __init__

    def commit(
            self,
            connection: Connection,
            address: Address,
            protocol: BaseProtocol
    ) -> None:
        """
        Handles the client.

        :param connection: The connection to the client.
        :param address: The address of the client.
        :param protocol: The communication protocol.
        """

        operator = Operator(
            operation=lambda: self.handle(
                connection=connection,
                address=address,
                protocol=protocol
            ),
            handler=Handler(
                exceptions=[ConnectionError],
                exception_callback=lambda: (
                    self.remove(operator=operator),
                    operator.stop()
                )
            ),
            termination=lambda: self.remove(operator=operator),
            block=True
        )

        self.operators.append(operator)

        operator.start_operation()
    # end commit

    def remove(self, operator: Operator) -> None:
        """
        Finishes the operation and removes the data.

        :param operator: The operator object.
        """

        try:
            self.operators.remove(operator)

        except ValueError:
            pass
        # end try
    # end remove

    def handle(
            self,
            connection: Connection,
            address: Address,
            protocol: BaseProtocol
    ) -> None:
        """
        Handles the client.

        :param connection: The connection to the client.
        :param address: The address of the client.
        :param protocol: The communication protocol.
        """

        received, address = protocol.receive(
            connection=connection, address=address
        )

        if received:
            self.respond(
                received=received,
                connection=connection,
                protocol=protocol
            )
        # end if
    # end handle

    def config_response(self) -> ConfigResponse:
        """
        Handles the client.

        :return: The data response.
        """

        return ConfigResponse(
            {
                "save": self.market.saving,
                "refresh": self.market.refresh,
                "limited": self.market.limited,
                "structure": self.market.structure(),
                "map": self.market.map()
            }
        )
    # end data_response

    def update_response(self, request: UpdateRequest) -> UpdateSuccessResponse:
        """
        Handles the client.

        :param request: The request from the client.

        :return: The data response.
        """

        if "refresh" in request.config:
            self.market.refresh = request.config["refresh"]
        # end if

        if "limited" in request.config:
            self.market.limited = request.config["limited"]
        # end if

        if "delay" in request.config:
            self.market.delay = request.config["delay"]
        # end if

        if "cancel" in request.config:
            self.market.cancel = request.config["cancel"]
        # end if

        if "save" in request.config:
            if not self.market.saving and request.config["save"]:
                self.market.start_saving()

            elif self.market.saving and not request.config["save"]:
                self.market.stop_saving()
            # end if
        # end if

        if "update" in request.config:
            if not self.market.updating and request.config["update"]:
                self.market.start_updating()

            elif self.market.updating and not request.config["update"]:
                self.market.stop_updating()
            # end if
        # end if

        return UpdateSuccessResponse()
    # end update_response

    def run_response(self) -> RunSuccessResponse:
        """
        Handles the client.

        :return: The data response.
        """

        self.market.run(block=False, save=False)

        return RunSuccessResponse()
    # end run_response

    def stop_response(self) -> StopSuccessResponse:
        """
        Handles the client.

        :return: The data response.
        """

        self.market.stop()

        return StopSuccessResponse()
    # end stop_response

    def pause_response(self) -> PauseSuccessResponse:
        """
        Handles the client.

        :return: The data response.
        """

        self.callback.disable()

        return PauseSuccessResponse()
    # end pause_response

    def unpause_response(self) -> UnpauseSuccessResponse:
        """
        Handles the client.

        :return: The data response.
        """

        self.callback.enable()

        return UnpauseSuccessResponse()
    # end unpause_response

    def response(self, request: ServiceRequest) -> ServiceResponse:
        """
        Handles the client.

        :param request: The request from the client.

        :return: The data response.
        """

        if isinstance(request, RunRequest):
            response = self.run_response()

        elif isinstance(request, StopRequest):
            response = self.stop_response()

        elif isinstance(request, ConfigRequest):
            response = self.config_response()

        elif isinstance(request, UpdateRequest):
            response = self.update_response(request=request)

        elif isinstance(request, PauseRequest):
            response = self.pause_response()

        elif isinstance(request, UnpauseRequest):
            response = self.unpause_response()

        else:
            response = RequestErrorResponse()
        # end if

        return response
    # end response

    def respond(
            self,
            received: bytes,
            connection: Connection,
            protocol: BaseProtocol
    ) -> None:
        """
        Handles the client.

        :param received: The received data.
        :param connection: The connection to the client.
        :param protocol: The communication protocol.
        """

        response = None
        request = None

        try:
            request = load_request(json.loads(received.decode()))

        except json.decoder.JSONDecodeError:
            response = JSONErrorResponse()

        except ValueError:
            response = DataErrorResponse()
        # end if

        if request is not None:
            response = self.response(request)
        # end if

        if isinstance(response, ServiceResponse):
            protocol.send(
                connection=connection,
                data=json.dumps(response.json()).encode()
            )
        # end if
    # end action
# end ArbitrageEventPublisher