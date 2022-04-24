pragma solidity ^0.4.25;

contract ERC20 {}

contract buy3 {

    string data = "";

    function transfer(address target, uint value) public payable
    {
        target.transfer(value);
    }

    function buy(ERC20 _token, address[] _exs, uint[] _indexs, uint256[] _values) public payable {
        for (uint i = 0; i < _exs.length; i++)
        {
            if (_token != address(0) && i > 0) {
                transfer(_token, _values[i]);
            } else {
                require(_exs[i].call.value(_values[i])(data), "");
            }
        }
    }
}