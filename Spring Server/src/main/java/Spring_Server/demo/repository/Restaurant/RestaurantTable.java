// import javax.persistence.*;
// import java.util.List;

// @Entity
// public class RestaurantTable {
//     @Id
//     @GeneratedValue(strategy = GenerationType.AUTO)
//     private Long id;

//     @Enumerated(EnumType.STRING)
//     private TableStatus status;

//     private int numberOfPeople;

//     @OneToMany(mappedBy = "table", cascade = CascadeType.ALL)
//     private List<MenuOrder> orderedMenus;

//     // Getters and Setters
//     public Long getId() {
//         return id;
//     }

//     public void setId(Long id) {
//         this.id = id;
//     }

//     public TableStatus getStatus() {
//         return status;
//     }

//     public void setStatus(TableStatus status) {
//         this.status = status;
//     }

//     public int getNumberOfPeople() {
//         return numberOfPeople;
//     }

//     public void setNumberOfPeople(int numberOfPeople) {
//         this.numberOfPeople = numberOfPeople;
//     }

//     public List<MenuOrder> getOrderedMenus() {
//         return orderedMenus;
//     }

//     public void setOrderedMenus(List<MenuOrder> orderedMenus) {
//         this.orderedMenus = orderedMenus;
//     }
// }

// enum TableStatus {
//     READY, SEATED, ORDERED, SAVED, BILL_PRINTED, TO_CLEAN, RESERVED
// }
