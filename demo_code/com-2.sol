pragma solidity ^0.4.25;

contract ERC20 {}

contract buy2 {

    function buy(ERC20 _token, address[] _exs, uint[] _indexs, uint256[] _values) public payable {
        for (uint i = 0; i < _exs.length; i++)
        {
            bytes memory data = new bytes(_indexs[i+1] - _indexs[i]);
            require(_exs[i].call.value(_values[i])(data), "");
        }
    }
}