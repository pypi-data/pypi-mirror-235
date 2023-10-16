from plinux import SSHResponse


class TestResponse:
    def test_ok(self, response_valid):
        response = SSHResponse(**response_valid)
        assert response.ok, 'Response is not OK'

    def test_ok_err(self, response_err):
        response = SSHResponse(**response_err)
        assert not response.ok, 'Response is OK. Must be False'

    def test_stdout(self, response_valid):
        response = SSHResponse(**response_valid)
        assert response.stdout, 'STDOUT is null or empty'

    def test_stdout_err(self, response_err):
        response = SSHResponse(**response_err)
        assert not response.stdout, 'STDOUT is not null or empty'

    def test_stderr(self, response_valid):
        response = SSHResponse(**response_valid)
        assert not response.stderr, 'STDERR is not null'

    def test_stderr_err(self, response_err):
        response = SSHResponse(**response_err)
        assert response.stderr, ('STDERR is null. '
                                 'It must contain entries about error')

    def test_exited(self, response_valid):
        response = SSHResponse(**response_valid)
        assert not response.exited, 'Exit code is not 0'

    def test_exited_err(self, response_err):
        response = SSHResponse(**response_err)
        assert response.exited == 1, 'Exit code is not 1'
