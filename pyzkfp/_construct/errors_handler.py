class ZKFP2Error(Exception):
    def __init__(self, message):
        super().__init__(message)

class DeviceAlreadyConnectedError(ZKFP2Error):
    ...

class DeviceNotInitializedError(ZKFP2Error):
    ...

class DeviceNotStartedError(ZKFP2Error):
    ...

class FailedToStartDeviceError(ZKFP2Error):
    ...

class FailedToCombineTemplatesError(ZKFP2Error):
    ...

class FingerprintComparisonFailedError(ZKFP2Error):
    ...

class CaptureCancelledError(ZKFP2Error):
    ...

class OperationFailedError(ZKFP2Error):
    ...

class FailedToDeleteTemplateError(ZKFP2Error):
    ...

class FailedToAddTemplateError(ZKFP2Error):
    ...

class FingerprintCapturedError(ZKFP2Error):
    ...

class InsufficientMemoryError(ZKFP2Error):
    ...

class AbortedError(ZKFP2Error):
    ...

class FailedToExtractTemplateError(ZKFP2Error):
    ...

class FailedToCaptureImageError(ZKFP2Error):
    ...

class InvalidHandleError(ZKFP2Error):
    ...

class InvalidParameterError(ZKFP2Error):
    ...

class NotSupportedError(ZKFP2Error):
    ...

class NoDeviceConnectedError(ZKFP2Error):
    ...

class CaptureLibraryInitializationError(ZKFP2Error):
    ...

class AlgorithmLibraryInitializationError(ZKFP2Error):
    ...

class UnknownError(ZKFP2Error):
    ...
