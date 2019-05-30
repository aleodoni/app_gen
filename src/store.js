let _store = {}

class SimpleStore {
    constructor(props) {
        if (props) {
            _store = props
        }
    }

    push(prop) {
        _store = {..._store, ...prop }
    }

    getContent() {
        return _store
    }
}

export default SimpleStore