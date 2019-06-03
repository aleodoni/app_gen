let _store: object = {}

class SimpleStore {
  public constructor (props: object) {
    if (props) {
      _store = props
    }
  }

  public push (prop) : void {
    _store = { ..._store, ...prop }
  }

  public getContent () : object {
    return _store
  }

  public getCurrDir () : string {
    return ''
  }
}

export default SimpleStore
