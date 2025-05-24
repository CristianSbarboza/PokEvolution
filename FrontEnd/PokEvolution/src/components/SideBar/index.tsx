import style from './style.module.css'

export function SideBar(){
  return <>
  <aside className={style.sideBar} >
    <button className={style.sideOptions}>Double Click <img src="https://static.thenounproject.com/png/1188209-200.png" alt="image" /></button>
    <button className={style.sideOptions}>+1 Pokeballl Bonus <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Pokebola-pokeball-png-0.png" alt="image" /></button>
    <button className={style.sideOptions}>Bucket Ball <img src="https://cdn-icons-png.flaticon.com/512/188/188942.png" alt="image" /></button>
  </aside>
  </> 
}